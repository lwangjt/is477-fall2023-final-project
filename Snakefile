
rule prepare:
    output:
        "data/rice+cammeo+and+osmancik.zip",
        "data/Rice_Cammeo_Osmancik.csv"
    shell:
        "python scripts/prepare_data.py"


rule profile:
    input:
        "data/Rice_Cammeo_Osmancik.csv"
    output:
        "profiling/report.html"
    shell:
        "python scripts/profile.py"

rule analyze:
    input:
        "data/Rice_Cammeo_Osmancik.csv"
    output:
        "results/confusion_matrix_testset.png",
        "results/results.txt"
    shell:
        "python scripts/analysis.py"

rule reproduce:
    input:
        "results/confusion_matrix_testset.png",
        "results/results.txt",
        "profiling/report.html"
