# app_ui.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image
import os
from utils import resource_path

class PhotoToPdfApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Photo To PDF")
        self.root.iconbitmap(resource_path("logo.ico"))
        self.root.geometry("520x612")
        self.image_paths = []

        # --- スタイルの設定 ---
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", padding=6, relief="flat", background="#ccc")
        style.map("TButton", background=[("active", "#e8e8e8")])

        # --- UIフレーム ---
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- 画像選択ボタン ---
        select_button = ttk.Button(
            main_frame, text="画像を選択", command=self.select_images
        )
        select_button.pack(fill=tk.X, pady=5)

        # --- 選択された画像リスト ---
        self.listbox = tk.Listbox(main_frame, selectmode=tk.MULTIPLE)
        self.listbox.pack(fill=tk.BOTH, expand=True, pady=5)

        # --- ボタンフレーム ---
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X)

        # --- 変換ボタン ---
        convert_button = ttk.Button(
            button_frame, text="PDFに変換", command=self.convert_to_pdf
        )
        convert_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        # --- クリアボタン ---
        clear_button = ttk.Button(
            button_frame, text="クリア", command=self.clear_list
        )
        clear_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))

        # --- 終了ボタン ---
        quit_button = ttk.Button(main_frame, text="終了", command=root.quit)
        quit_button.pack(fill=tk.X, pady=5)

    def select_images(self):
        files = filedialog.askopenfilenames(
            title="画像ファイルを選択",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"),
                ("All files", "*.*"),
            ],
        )
        if files:
            for file in files:
                if file not in self.image_paths:
                    self.image_paths.append(file)
                    self.listbox.insert(tk.END, os.path.basename(file))

    def clear_list(self):
        self.listbox.delete(0, tk.END)
        self.image_paths = []

    def convert_to_pdf(self):
        if not self.image_paths:
            messagebox.showwarning("警告", "画像が選択されていません。")
            return

        save_path = filedialog.asksaveasfilename(
            title="PDFを保存",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
        )

        if not save_path:
            return

        try:
            images = []
            # 最初の画像をRGBで開く
            img1 = Image.open(self.image_paths[0]).convert("RGB")
            
            # 残りの画像を処理
            for path in self.image_paths[1:]:
                img = Image.open(path).convert("RGB")
                images.append(img)

            img1.save(save_path, save_all=True, append_images=images)
            messagebox.showinfo("成功", f"PDFが正常に保存されました:\n{save_path}")
            self.clear_list()
        except Exception as e:
            messagebox.showerror("エラー", f"PDF変換中にエラーが発生しました:\n{e}")