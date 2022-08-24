import pandas

# read the casv into pandas dataframe
file = pandas.read_csv("test_data.csv")
file["insight"] = ""

#iterate through rows of file
for index, row in file.iterrows():


#convert text column data to lower in prep for comparison
    text = row["text"].lower()

#check for text in rows for client
    if row["role"] == "manager":

        #if greetings found ibn row text mark by printint(note that pritning is temporary
        if "алло" in text or "здравствуйте" in text or "добрый день" in text:
            file.insight[index] = "greetings = True"

        #if name indicator is in row print
        if "зовут" in text:
            file.insight[index] = "name mention = True"

        # if company indicator is in row print
        if "компания" in text:
            file.insight[index] = "company mention = True"

        #if goodbye is in row text print
        if "до свидания" in text or "всего доброго" in text:
            file.insight[index] = "Goodbye = True"

file.to_csv("test_data.csv", sep=',', index=False)





