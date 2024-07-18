from resume_parser import resumeparse


def resume_parse(file):
    data = resumeparse.read_file(file)
    for i, j in data.items():
        print(f"{i}:>>{j}")


sample = "resume_001.docx"
resume_parse(sample)
