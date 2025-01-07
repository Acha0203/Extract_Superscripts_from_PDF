import pymupdf  # PyMuPDF

def extract_subscripts(pdf_path):
    subscripts = []

    # PDFを開く
    with pymupdf.open(pdf_path) as doc:
        for page_num, page in enumerate(doc, start=1):
            blocks = page.get_text("dict")["blocks"]  # テキストブロックを取得

            for block in blocks:
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        # フォントサイズとY座標を取得
                        font_size = span["size"]
                        origin_y = span["origin"][1]  # Y座標

                        # 文字が小さいかつ、Y座標が基準よりも低い場合を下付き文字として特定
                        if font_size < 7 and origin_y - font_size / 2 > 0:
                            subscripts.append({
                                "text": span["text"],
                                "page": page_num,
                                "size": font_size,
                                "position": span["origin"]
                            })

    return subscripts

# 使用例
pdf_path = "ADG5298.pdf"  # PDFファイルのパス
subscripts = extract_subscripts(pdf_path)

# 結果をファイルに書き出し
output_file = "subscripts.txt"  # 出力ファイルのパス

with open(output_file, "w") as f:
    if subscripts:
        for item in subscripts:
            f.write(f"Page {item['page']}: {item['text']} (Font Size: {item['size']}, Position: {item['position']})\n")
    else:
        f.write("下付き文字は見つかりませんでした。\n")

print(f"結果は {output_file} に書き出されました。")
