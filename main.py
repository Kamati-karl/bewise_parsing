import pandas

# read the casv into pandas dataframe
file = pandas.read_csv("test_data - test_data.csv")

#i9terate through rows of file
for index, row in file.iterrows():
#convert text column data to lower in prep for comparison
    text = row["text"].lower()
#check for text in rows for client
    if row["role"] == "client":
        #if greetings found ibn row text mark by printint(note that pritning is temporary
        if "алло" in text or "здравствуйте" in text or "добрый день" in text:
            print(f"greeting ","dialogue number: ", row["dlg_id"], "line number: ",row["line_n"],"role: ", row["role"])
        #if name indicator is in row print
        if "зовут" in text:
            print( print(f"name ","dialogue number: ", row["dlg_id"], "line number: ",row["line_n"],"role: ", row["role"]))
        # if company indicator is in row print
        if "компания" in text:
            print( print( print(f"company ","dialogue number: ", row["dlg_id"], "line number: ",row["line_n"],"role: ", row["role"])))
        #if goodbye is in row text print
        if "до свидания" in text or "всего доброго" in text:
            print(f"goodbye ", "dialogue number: ", row["dlg_id"], "line number: ", row["line_n"], "role: ",
                  row["role"])






