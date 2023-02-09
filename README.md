# Guestbook
This is a command line application that allows the user to create, read, update, and delete notes in a guestbook.

##### Getting Started

Clone the repository:
```sh
	git clone https://github.com/airrloww/guestbook.git 
```

Run the script:
```sh
	python guestbook.py 
```

##### Usage
The following commands are available:
* new: Add a new note to the guestbook
* list: Show all notes in the guestbook
* edit: Edit a note in the guestbook
* delete: Delete a note in the guestbook
* export: Export the guestbook in json format

##### Examples
Adding a new note:
```sh
python guestbook.py new "This is a new note" 
```
Listing all notes:
```sh
python guestbook.py list
```
Editing a note:
```sh
python guestbook.py edit 1 "This is an edited note" 
```
Deleting a note:
```sh 
python guestbook.py delete 1 
```
Exporting the guestbook in json format:
```sh
python guestbook.py export 
```
###### Note
The notes are stored in a json file named guestbook.txt in the root directory of the project.

Built With
* Python
* Click
* JSON
