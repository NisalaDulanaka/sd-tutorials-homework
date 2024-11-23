
#Beginner
def count_file_chars(file_path: str):
    file=None
    try:
        file=open(file_path, "r")
        f_lines=file.readlines()

        char_count=0
        for line in f_lines:
            char_count+=len(line)

        print("Character count: ",char_count)
    except:
        print("Cannot find file")
    finally:
        file.close()

def write_hello_world_file():
    file=open(".\\week-8\\greetings.txt", "w")
    file.writelines("Hello\nWorld")

#Intermediate
def line_analysis():
    try:
        file=open(".\\week-8\\data.txt", "r")
        content=file.readlines()
        for line in content:
            print(f"Line: {line} Length:{len(line)}\n")
    except:
        print("File not found")

def fin_replace():
    try:
        file=open(".\\week-8\\story.txt", "r")
        content=file.readlines()
        for index in range(len(content)):
            content[index] = content[index].replace("Python","Pythons")

        new_file=open(".\\week-8\\modified_story.txt", "w")
        new_file.writelines(content)
    except:
        print("File not found")

#Advanced Level
def generate_summary():
    try:
        file=open(".\\week-8\\reviews.txt", "r")
        content=file.readlines()
        line_count=len(content)

        total_rating=0
        for index in range(line_count):
            line=content[index].strip()
            total_rating += int(line.split(",")[1])

            average=total_rating/line_count
            summary=f"<------ SUMMARY REPORT ------>\n\nTOTAL REVIEWS: {total_rating}\nAVERAGE RATING: {average}"
            
            new_file=open(".\\week-8\\summary.txt", "w")
            new_file.writelines(summary)
    except:
        print("File not found")

def manipulate_content():
    to_replace=input("Enter the word you want to replace: ")
    replace_with=input("Enter the word you want to replace with: ")

    try:
        file=open(".\\week-8\\article.txt", "r")
        content=file.readlines()
        for index in range(len(content)):
            line=content[index]
            line = line.replace(to_replace, replace_with).strip()
            content[index] = line.capitalize() + "\n"

        new_file=open(".\\week-8\\formatted_article.txt", "w")
        new_file.writelines(content)
    except:
        print("File not found")

manipulate_content()
