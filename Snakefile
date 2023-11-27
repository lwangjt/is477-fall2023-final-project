rule prepare_data.py:
  output:
    "rice+cammeo+and+osmancik.zip",
  shell:
    "python lab6/step1.py"
rule profile.py:
  output:
    "lab6/output3.txt"
  shell:
    "python lab6/step2.py"
rule analyze.py:
  input:
    "lab6/output3.txt"
  output:
    "results/results.txt",
    "results/confusion_matrix_testset.png"
  shell:
    "python lab6/step3.py"