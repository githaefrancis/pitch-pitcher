# Pitch Pitcher

## Description
This is a Flask application that allows a user to create and post pitches.The user gets a welcoming message on registering on the application The pitches can fall under pickup line, interview, product pitch and promotional pitch categories. The user can view , downvote, upvote and comment on pitches including pitches from other users.


## Author

Francis Githae

# Technologies

Python 3.8.10
Flask
Bootstrap
Fontawesome
JQuery

# Features
- Register for a account
- Login 
- Post a pitch
- View pitch
- Downvote a pitch
- Upvote a pitch
- Filter pitches by category
- Update profile picture
- View pitches you have posted.


## Setup and Installation

1. Clone the repository

```bash
git@github.com:githaefrancis/pitch-pitcher.git
```

2. Navigate to project folder

```bash
cd pitch-pitcher
```

3. Create a virtual environment
```
python3 -m venv <name>
```

4. Activate the virtual environment

source <name>/bin/activate

5. Install dependencies

```
pip intall -r requirements.txt
```

6. Create the .env variables in the root folder
```bash
touch .env
```
Create the environment  variables

export SECRET_KEY='<Your Secret Key>'

7. Load the environment variables

```bash
source .env
```
4. Grant the python executable permissions

```
chmod +x start.sh
```
5. Run the application

```
./start.sh
```

## Live Link

[Pitch Pitcher](https://pitch-pitcher.herokuapp.com/ )

## Contact
Email: mureithigithae@gmail.com

## License

This project is under the MIT License [click here for more information](LICENSE)

&copy; 2022 Francis Githae