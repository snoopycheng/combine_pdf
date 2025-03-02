from PyPDF2 import PdfMerger

# test to upload  to github

merger = PdfMerger()

merger.append("test1.pdf")
merger.append("test2.pdf")

merger.write("test3.pdf")
merger.close()

print("finish0")

# 不含致謝

# merger = PdfMerger()

# merger.append("Abstract_Acknowledgements.pdf")
# merger.append("LCLSH_thesis_final_modified.pdf")

# merger.write("LCLSH_thesis_final_modified_test.pdf")
# merger.close()

# print("finish1")


# 含致謝

# merger = PdfMerger()

# merger.append("Abstract_Acknowledgements_all.pdf")
# merger.append("LCLSH_thesis_final_modified.pdf")

# merger.write("LCLSH_thesis_final_modified_all.pdf")
# merger.close()

# print("finish2")


# 中英文摘要

# merger = PdfMerger()

# merger.append("Abstract_chinese.pdf")
# merger.append("Abstract_eng.pdf")

# merger.write("Abstract_all.pdf")
# merger.close()

# print("finish3")


# 要拿去印的

# merger = PdfMerger()

# merger.append("Abstract_Acknowledgements_head_only.pdf")
# merger.append("清大圖書館授權書.pdf")
# merger.append("國家圖書館授權書.pdf")
# merger.append("指導教授推薦書.pdf")
# merger.append("考試委員審定書.pdf")
# merger.append("Abstract_Acknowledgements_without_head.pdf")
# merger.append("LCLSH_thesis_final_modified.pdf")

# merger.write("LCLSH_thesis_final_all_print.pdf")
# merger.close()

# print("finish4")