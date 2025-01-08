import pymupdf  # PyMuPDF
import sys
import os

def extract_subscripts(pdf_path, threshold):
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
                        if font_size <= threshold and origin_y - font_size / 2 > 0:
                            subscripts.append({
                                "text": span["text"],
                                "page": page_num,
                                "size": font_size,
                                "position": span["origin"]
                            })

    return subscripts

input_file_name = ""

while input_file_name == "":
    print('下付き文字のテキストを抽出したいPDFのファイル名を「XXX.pdf」の形式で入力してください: ')
    sys.stdout.flush()
    input_file_name = str(sys.stdin.readline()).strip()
    if not os.path.exists(input_file_name):
        print(f"ファイル {input_file_name} が存在しません。ファイル名を確認してください。")
        input_file_name = ""

print(f"{input_file_name} から下付き文字のテキストを抽出します。")
print('抽出する下付き文字の大きさを数値で入力してください。デフォルトは「8.5」です: ')
sys.stdout.flush()
threshold_input = sys.stdin.readline().strip()

if threshold_input == "":
    threshold = 8.5
else:
    threshold = int(threshold_input)

print('結果を出力するテキストファイルの名前を「XXX.txt」の形式で入力してください。デフォルトのファイル名は「subscripts.txt」です: ')
sys.stdout.flush()
output_file_name = str(sys.stdin.readline()).strip()

if output_file_name == "":
    output_file_name = "subscripts.txt"

subscripts = extract_subscripts(input_file_name, threshold)

# 結果をファイルに書き出し
with open(output_file_name, "w") as f:
    if subscripts:
        for item in subscripts:
            f.write(f"Page {item['page']}: {item['text']} (Font Size: {item['size']}, Position: {item['position']})\n")
    else:
        f.write("下付き文字は見つかりませんでした。\n")

print(f"結果は {output_file_name} に書き出されました。")
