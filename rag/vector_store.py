"""
Pleadly RAG 向量数据库模块
ChromaDB + sentence-transformers Embedding
"""

import os
import chromadb
from typing import List, Dict, Optional
from sentence_transformers import SentenceTransformer

# ── Config ──
CHROMA_PATH = os.getenv("CHROMA_PERSIST_PATH", "./chroma_data")
EMBEDDING_MODEL = "shibing624/text2vec-base-chinese"  # 免费中文向量模型

# ── Singleton ──
_chroma_client: Optional[chromadb.PersistentClient] = None
_embedding_model: Optional[SentenceTransformer] = None

def get_chroma_client() -> chromadb.PersistentClient:
    global _chroma_client
    if _chroma_client is None:
        os.makedirs(CHROMA_PATH, exist_ok=True)
        _chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    return _chroma_client

def get_embedding_model() -> SentenceTransformer:
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = SentenceTransformer(EMBEDDING_MODEL)
    return _embedding_model

# ── Embedding ──

def embed_texts(texts: List[str]) -> List[List[float]]:
    """将文本列表转为向量。"""
    model = get_embedding_model()
    embeddings = model.encode(texts, normalize_embeddings=True)
    return embeddings.tolist()

def embed_query(query: str) -> List[float]:
    """将查询文本转为向量。"""
    return embed_texts([query])[0]

# ── Collection Management ──

COLLECTIONS = {
    "interviews": "面试题库 — 按行业/岗位分类的真实面试题和回答模板",
    "companies": "公司信息库 — 常见公司的背景、文化、面试流程",
    "salaries": "行业薪资数据 — 各城市/岗位的薪资分位数据",
    "templates": "简历模板库 — 不同行业/岗位的优秀简历模板和STAR改写案例",
}

def get_or_create_collection(name: str) -> chromadb.Collection:
    """获取或创建ChromaDB集合。"""
    client = get_chroma_client()
    try:
        return client.get_collection(name)
    except:
        return client.create_collection(
            name=name,
            metadata={"description": COLLECTIONS.get(name, "")}
        )

def add_documents(collection_name: str, texts: List[str], metadatas: List[Dict] = None):
    """向知识库添加文档。"""
    collection = get_or_create_collection(collection_name)
    embeddings = embed_texts(texts)
    ids = [f"{collection_name}_{i}" for i in range(len(texts))]

    # Remove existing docs with same IDs
    try:
        collection.delete(ids=ids)
    except:
        pass

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=texts,
        metadatas=metadatas or [{}] * len(texts),
    )

def search_documents(
    collection_name: str,
    query: str,
    n_results: int = 5,
) -> List[Dict]:
    """在知识库中检索相关文档。"""
    try:
        collection = get_or_create_collection(collection_name)
        query_embedding = embed_query(query)
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
        )
        docs = []
        for i in range(len(results['documents'][0])):
            docs.append({
                "content": results['documents'][0][i],
                "metadata": results['metadatas'][0][i] if results['metadatas'] else {},
                "distance": results['distances'][0][i] if results['distances'] else 0,
            })
        return docs
    except Exception as e:
        return [{"content": f"检索出错: {e}", "metadata": {}, "distance": 0}]

def search_all(query: str, n_results: int = 3) -> Dict[str, List[Dict]]:
    """在所有知识库中检索。"""
    results = {}
    for coll_name in COLLECTIONS:
        docs = search_documents(coll_name, query, n_results)
        if docs and docs[0].get("content"):
            results[coll_name] = docs
    return results

# ── Data Ingestion Helpers ──

def ingest_text_file(collection_name: str, file_path: str):
    """从文本文件导入数据到知识库。每行作为一个独立文档。"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    add_documents(collection_name, lines)
    print(f"✅ 已导入 {len(lines)} 条记录到 {collection_name}")

def ingest_markdown_files(collection_name: str, directory: str):
    """从目录中的Markdown文件导入，每个文件作为一个文档。"""
    import glob
    texts = []
    for md_file in glob.glob(f"{directory}/*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            texts.append(f.read())
    add_documents(collection_name, texts)
    print(f"✅ 已导入 {len(texts)} 个文档到 {collection_name}")

if __name__ == "__main__":
    print("🧠 Pleadly RAG 向量数据库模块")
    print(f"   模型: {EMBEDDING_MODEL}")
    print(f"   存储: {CHROMA_PATH}")
    print(f"   支持集合: {list(COLLECTIONS.keys())}")
