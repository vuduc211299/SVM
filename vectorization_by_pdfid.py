def splitBrackets(number):
    result = []
    if "(" not in number:
        result = [int(number)]
    else:
        # part2 = number.split("(")[1]
        # num2 = int(part2.split(")")[0])
        result = [int(number.split("(")[0])]
    return result

dataset = []
target = []

with open("malicious_log.txt") as f:
    lines = f.readlines()
    i = 0
    malicious_dataset = []
    malicious_target = []
    while i < len(lines):
        if "PDFiD 0.2.7" in lines[i]:
            if "PDF Header" in lines[i+1]:
                v = []				
                i += 1
                #header = ''.join(lines[i].split()[1:])
                #if header in PDFHeaders:
                #	PDFHeaders[header] += 1
                #else:
                #	PDFHeaders[header] = 1
                i += 1
                #obj				
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #endobj
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #stream
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1			
                #endstream
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #xref
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1				
                #trailer
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #startxref
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #Page
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #Encrypt
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #ObjStm
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #JS
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #JavaScript
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #AA
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #OpenAction
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #AcroForm
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #JBIG2Decode
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #RichMedia
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #Launch
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #EmbeddedFile
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #XFA
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #URI
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #Colors
                v.append(splitBrackets(lines[i].split()[3])[0])

                # print("array", v, len(v))

                malicious_dataset.append(v)
                malicious_target = [-1] * len(malicious_dataset)

        i += 1


with open("log.txt") as f:
    lines = f.readlines()
    i = 0
    benign_dataset = []
    benign_target = []
    while i < len(lines):
        if "PDFiD 0.2.7" in lines[i]:
            if "PDF Header" in lines[i+1]:
                v = []				
                i += 1
                #header = ''.join(lines[i].split()[1:])
                #if header in PDFHeaders:
                #	PDFHeaders[header] += 1
                #else:
                #	PDFHeaders[header] = 1
                i += 1
                #obj				
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #endobj
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #stream
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1			
                #endstream
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #xref
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1				
                #trailer
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #startxref
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #Page
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #Encrypt
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #ObjStm
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #JS
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #JavaScript
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #AA
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #OpenAction
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #AcroForm
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #JBIG2Decode
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #RichMedia
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #Launch
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #EmbeddedFile
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #XFA
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #URI
                v.append(splitBrackets(lines[i].split()[1])[0])
                i += 1
                #Colors
                v.append(splitBrackets(lines[i].split()[3])[0])

                # print("array", v, len(v))

                benign_dataset.append(v)
                benign_target = [1] * len(benign_dataset)

        i += 1

dataset = malicious_dataset + benign_dataset
target = malicious_target + benign_target
