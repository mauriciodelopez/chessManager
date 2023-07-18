# Chess tournament manager : ♟️♟️♟️♟️
This program was created as part of OpenClassrooms Project 4. It is a chess tournament manager.

# Setup : 😀
Start by installing Python. Then launch the console, move to the folder of your choice and clone the repository:

```python
git clone https://github.com/mauriciodelopez/chessManager.git
```

Go to the chessManager folder, then create a new virtual environment:

```python
python -m venv env
```

Then activate it. Windows:

```python
env\scripts\activate.bat
```

Linux & Mac OS :

```python
source env/bin/activate
```

All that remains is to install the required packages:

```python
pip install -r requirements.txt
```

Now you can run the script:

```python
python main.py
```

# Usage
The main menu is split into 7 options.

1 ▻ Create a tournament :

The program lets you manage chess tournaments. When using it for the first time, select "Create a tournament", then let us guide you.

♟️ If there are no players in the database, you will be prompted to create one.

♟️ You can also choose "DEFAULT", and use the players in the database. 

♟️ During a tournament, you will be asked to enter the results after each match. At the end of a tournament, a ranking will be generated.

♟️ During a tournament, you'll be able to save the current tournament, load a new one, view or modify rankings.

2 ▻ Create players :

When you select this option, you will be prompted to enter the number of players to be created.
Then let the program guide you.

3 ▻ Get_player to tournament :

When you select this option, you will be prompted to select 8 players & enter their #ID to be created.
Then let the program guide you.

4 ▻ Reports :

♟️This section allows you to generate various reports.

♟️You can view: overall player rankings by ranking and alphabetical order.

♟️Details of current and past tournaments: tournament player rankings, rounds and matches of each tournament, also match results.

5 ▻ Default :

This section lets you create different players from a default database.
Then let the program guide you.

6 ▻ Resume tournament :

This section allows you to view the number of the just completed tournament and the winner of the tournament.

7 ▻ Generate JSON file :

This section allows you to view :

♟️tournament details.

♟️the list of players in the tournament with their details.

♟️details of each round and match.

♟️the score of each match.

♟️the color of the figures.

♟️tournament winner.

# Generation of flake8 repport

This section allows you to create a flake8 repport :

install flake8 with the commande:

```python
pip install flake8-html
```

If doesn't exist, please to create setup.cfg file
Write the next text:

```python
[flake8]
exclude = .git, env, __pycache__, .gitignore
max-line-length = 119
```
Enter the command : 

```python
flake8 --format=html --htmldir=flake8_report
```






