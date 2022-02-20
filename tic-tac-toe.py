# Tic Tac Toe Bot, a simple discord bot to play tic tac toe with another person on a discord server
# Copyright (C) 2022  Antoine Meloche

import discord
import time

class TicTacToe(discord.Client):

    player1 = None
    player2 = None
    p = [
        '-',
        '-',
        '-',
        '-',
        '-',
        '-',
        '-',
        '-',
        '-'
    ]
    plays = 0
    win = False


    async def on_ready(self):
        print(f'Bot has logged in as {client.user}')
        await client.change_presence(activity=discord.Activity(name='*help for commands', type=0)) 

    async def on_message(self,message):
        if message.author == client.user:
            return


        if message.content.startswith('*help'):
            await message.channel.send('```*tic: set player 1\n*tac: set player 2\n*toe: show the board\n*play #: place your mark at spot #\n*reset: reset the game\n*players: see the current players\n*board: show the spots on the board```')
        

        if message.content.startswith('*board'):
            await message.channel.send('1 | 2 | 3\n-------\n4 | 5 | 6\n-------\n7 | 8 | 9')


        if message.content.startswith('*tic') and self.player1 != None:
            await message.channel.send("There is already a Player 1, try '*tac'")
            return

        if message.content.startswith('*tic'):
            self.player1 = message.author
            await message.channel.send(f'Player 1: {self.player1}')


        if message.content.startswith('*tac') and self.player1 == None:
            await message.channel.send("Player 1 is not set, use *tic before '*tac'")
            return

        if message.content.startswith('*tac') and message.author == self.player1:
            await message.channel.send("Player 1 cannot be the same as player 2")
            return

        if message.content.startswith('*tac'):
            self.player2 = message.author
            await message.channel.send(f'Player 2: {self.player2}')


        if message.content.startswith('*toe'):
              await message.channel.send(f"{self.p[0]} | {self.p[1]} | {self.p[2]}\n-------\n{self.p[3]} | {self.p[4]} | {self.p[5]}\n-------\n{self.p[6]} | {self.p[7]} | {self.p[8]}")

        
        if message.content.startswith('*players'):
            await message.channel.send(f'Player 1: {self.player1}, Player 2: {self.player2}')


        if message.content.startswith('*reset'):
            self.player1 = None
            self.player2 = None
            self.p = [
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-'
            ]
            self.plays = 0
            self.win = False

            await message.channel.send('Tic Tac Toe Reset')


        if message.content.startswith('*play'):
            move = int(message.content.split('*play ')[1]) - 1

            if move > 8:
                return

            if self.p[move] != '-':
                await message.channel.send('That spot is taken try another')
                await message.channel.send(f"{self.p[0]} | {self.p[1]} | {self.p[2]}\n-------\n{self.p[3]} | {self.p[4]} | {self.p[5]}\n-------\n{self.p[6]} | {self.p[7]} | {self.p[8]}")
                return

            if message.author == self.player1:
                if self.plays % 2 == 1:
                    return
                self.p[move] = 'O'
            if message.author == self.player2:
                if self.plays % 2 == 0:
                    return
                self.p[move] = 'X'
            
            self.plays += 1
            await message.channel.send(f"{self.p[0]} | {self.p[1]} | {self.p[2]}\n-------\n{self.p[3]} | {self.p[4]} | {self.p[5]}\n-------\n{self.p[6]} | {self.p[7]} | {self.p[8]}")

            if self.p[0] == self.p[1] == self.p[2]:
                if self.p[0] == 'O':
                    await message.channel.send(f'{self.player1.mention} has won the Game')
                    self.win = True
                if self.p[0] == 'X':
                    await message.channel.send(f'{self.player2.mention} has won the Game!')
                    self.win = True
                if self.p[0] == '-':
                    return
            
            if self.p[0] == self.p[3] == self.p[6]:
                if self.p[0] == 'O':
                    await message.channel.send(f'{self.player1.mention} has won the Game')
                    self.win = True
                if self.p[0] == 'X':
                    await message.channel.send(f'{self.player2.mention} has won the Game!')
                    self.win = True
                if self.p[0] == '-':
                    return
            
            if self.p[2] == self.p[5] == self.p[8]:
                if self.p[2] == 'O':
                    await message.channel.send(f'{self.player1.mention} has won the Game')
                    self.win = True
                if self.p[2] == 'X':
                    await message.channel.send(f'{self.player2.mention} has won the Game!')
                    self.win = True
                if self.p[2] == '-':
                    return

            if self.p[6] == self.p[7] == self.p[8]:
                if self.p[6] == 'O':
                    await message.channel.send(f'{self.player1.mention} has won the Game')
                    self.win = True
                if self.p[6] == 'X':
                    await message.channel.send(f'{self.player2.mention} has won the Game!')
                    self.win = True
                if self.p[6] == '-':
                    return

            if self.p[0] == self.p[4] == self.p[8]:
                if self.p[0] == 'O':
                    await message.channel.send(f'{self.player1.mention} has won the Game')
                    self.win = True
                if self.p[0] == 'X':
                    await message.channel.send(f'{self.player2.mention} has won the Game!')
                    self.win = True
                if self.p[0] == '-':
                    return

            if self.p[2] == self.p[4] == self.p[6]:
                if self.p[2] == 'O':
                    await message.channel.send(f'{self.player1.mention} has won the Game')
                    self.win = True
                if self.p[2] == 'X':
                    await message.channel.send(f'{self.player2.mention} has won the Game!')
                    self.win = True
                if self.p[2] == '-':
                    return
            
            if self.p[1] == self.p[4] == self.p[7]:
                if self.p[2] == 'O':
                    await message.channel.send(f'{self.player1.mention} has won the Game')
                    self.win = True
                if self.p[2] == 'X':
                    await message.channel.send(f'{self.player2.mention} has won the Game!')
                    self.win = True
                if self.p[2] == '-':
                    return

            if self.win == False and self.plays != 9:
                return

            if self.win == False and self.plays == 9:
                await message.channel.send('Tie!')

            self.player1 = None
            self.player2 = None
            self.p = [
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-'
            ]
            self.plays = 0
            self.win = False

try:
	with open("token.txt", "r") as f:
		token = f.read()
except Exception:
	print("No `token.txt` file was found in current directory")

client = TicTacToe()
client.run(token)
