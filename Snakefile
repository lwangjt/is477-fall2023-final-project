
rule prepare:
    output:
        "rice+cammeo+and+osmancik.zip",
        "Rice_Cammeo_Osmancik.csv"
    shell:
        "python prepare_data.py"


rule profile:
    input:
        "Rice_Cammeo_Osmancik.csv"
    output:
        "report.html"
    shell:
        "python profile.py"

rule analyze:
    input:
        "Rice_Cammeo_Osmancik.csv",
    output:
        "confusion_matrix_testset.png",
        "results.txt"
    shell:
        "python analysis.py"
