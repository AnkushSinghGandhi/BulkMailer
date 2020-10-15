[![MastHead](https://raw.githubusercontent.com/ankushsinghgandhi/template-project-repo/main/header.jpg)](https://ankushsinghgandhi.github.io)
<p align="center">
  <a href="https://ankushsinghgandhi.github.io">
    <img src="https://img.shields.io/badge/Website-3b5998?style=flat-square&logo=google-chrome&logoColor=white" />
  </a>
  <a href="http://twitter.com/ankushsgandhi">
    <img src="https://img.shields.io/badge/-Twitter-blue?style=flat-square&logo=twitter&logoColor=white" />
  </a>
   <a href="https://www.linkedin.com/in/ankush-singh-gandhi-2487771aa/">
    <img src="https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=Linkedin&logoColor=white" />
  </a>
  <a href="https://dev.to/@ankushsinghgandhi">
    <img src="https://img.shields.io/badge/-Dev.to-grey?style=flat-square&logo=dev.to&logoColor=white"/>
  </a>
  <a href="https://stackoverflow.com/users/13790266/ankush-singh">
    <img src="https://img.shields.io/badge/-Stackoverflow-orange?style=flat-square&logo=stackoverflow&logoColor=white"/>
  </a>
  <a href="https://leetcode.com/ankushsinghgandhi/">
    <img src="https://img.shields.io/badge/-Leetcode-yellow?style=flat-square&logo=Leetcode&logoColor=white"/>
  </a>
    <a href="https://www.hackerrank.com/ankushsgandhi">
    <img src="https://img.shields.io/badge/-HackerRank-green?style=flat-square&logo=Hackerrank&logoColor=white"/>
  </a>
</p>



# Bulk Mailer
## Send bulk mails all at once running Python Script which includes features like HTML mail, attach files and read contacts from excel.

<center>
<div>
    <img src='./src/giphy.gif' style="width:80%; height:50%"></img>
</div>
</center>

### How to use
- clone this repo
```
$ git clone https://github.com/swaaz/Bulk-Mailer.git
```

- change directory
```
$ cd Bulk-Mailer
```

- click on this [link](https://myaccount.google.com/lesssecureapps) and turn this option on as shown below

<img src="./src/img1.png">
<img src="./src/img2.png">

- open any editor of your choice and edit main.py
replace mailid and password
```
mailid   = "enter mail-id"
password = "password"
```
### Note: choose any one option depending upon your choice and delete other option
#### option-1: if you want to send mail with content
#### option-2: if you want to send HTML mail

### Attach files
if you need to attach files along wih this mail then paste all the files inside ```Bulk-Mailer/attachments/``` 

### Contacts
create a excel sheet named ```contacts.xlsx``` and name the coloumn as ```mail id``` and store all the mail id under that column
if you want to add mail id manually then replace this code snippet 
```
# reading mail id's from excel sheet
cont = pd.read_excel("contacts.xlsx")
contacts = cont['mail id'].values  #storing all the mail id's in contacts list
```
with this code
```
contacts = ['mailid1@gmail.com', 'mailid2@gmail.com']
```

### bugs
if you find any bugs then feel free to create issue and tag [@swaaz](https://github.com/swaaz/) 


#

<div align="center">

### Show some ❤️ by starring some of the repositories!

</div>
