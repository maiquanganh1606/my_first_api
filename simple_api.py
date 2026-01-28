from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <--- Thêm cái này

app = FastAPI()

# --- CẤU HÌNH CORS (MỞ KHÓA KẾT NỐI) ---
# Cho phép mọi trang web đều có thể gọi vào API này
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # "*" nghĩa là cho phép tất cả
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/kiem-tra/{con_so}")
def may_chan_le(con_so: int):
    if con_so % 2 == 0:
        ket_qua = "SỐ CHẴN"
    else:
        ket_qua = "SỐ LẺ"

    return {
        "so_ban_nhap": con_so,
        "ket_qua": ket_qua
    }