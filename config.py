import os
from dotenv import load_dotenv

# ==========================================================
# Load Environment Variables
# ==========================================================
load_dotenv()

# ==========================================================
# Application
# ==========================================================
APP_NAME = "DocsHelp"
APP_VERSION = "1.0.0"

# ==========================================================
# AI Providers
# ==========================================================
DEFAULT_PROVIDER = "auto"

OMNIROUTE_API_KEY = os.getenv("OMNIROUTE_API_KEY")
OMNIROUTE_BASE_URL = os.getenv(
    "OMNIROUTE_BASE_URL",
    "http://localhost:20128/v1"
)

# ==========================================================
# Models
# ==========================================================
OMNIROUTE_MODEL = os.getenv("OMNIROUTE_MODEL")

# ==========================================================
# ChromaDB
# ==========================================================
CHROMA_DB_PATH = "data/chroma_db"
COLLECTION_NAME = "docshelp"

# ==========================================================
# Embeddings
# ==========================================================
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==========================================================
# Upload Settings
# ==========================================================
UPLOAD_FOLDER = "data/uploads"

SUPPORTED_FILE_TYPES = [
    "pdf"
]

MAX_UPLOAD_SIZE_MB = 200

# ==========================================================
# Text Chunking
# ==========================================================
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# ==========================================================
# Retrieval Settings
# ==========================================================
RETRIEVAL_TOP_K = 8

MAX_CONTEXT_CHUNKS = 8

# ==========================================================
# UI Settings
# ==========================================================
SIDEBAR_STATE = "expanded"

LAYOUT = "wide"

# ==========================================================
# Theme Colors
# ==========================================================
PRIMARY_COLOR = "#2563EB"

SUCCESS_COLOR = "#16A34A"

WARNING_COLOR = "#F59E0B"

ERROR_COLOR = "#DC2626"

BACKGROUND_COLOR = "#FFFFFF"

SIDEBAR_COLOR = "#F8FAFC"

BORDER_COLOR = "#E5E7EB"

TEXT_COLOR = "#111827"

# ==========================================================
# Session Keys
# ==========================================================
SESSION_DOCUMENT = "current_document"

SESSION_PAGE_COUNT = "page_count"

SESSION_CHUNK_COUNT = "chunk_count"

SESSION_MESSAGES = "messages"

SESSION_QUIZ = "quiz"