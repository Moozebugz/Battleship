#Libraries
import pygame
pygame.init()

#Text and booleans
drawing = True
turn2 = False
turn1 = True

print("---------- Rules and Info -------------")
print("The playing area is a 5 by 5 grid!")
print("Your ships are kept in one tile!")
print("To place your ship, pick a number between 1 and 25!")
print("The person who loses all ships first loses the game!")

#Ship placements
a = input("Player 1 where would you like to put your ship? (1 - 25) ")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
b = input("Player 2 where would you like to put your ship? (1 - 25) ")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

a = int(a)
b = int(b)

#Setup
window = pygame.display.set_mode([400, 400])
c = pygame.time.Clock()
rects = []

#For loops (thanks abbas!)
for i in range(5):
    rect = pygame.Rect(i * 80, 0, 80, 80)
    rects.append([rect, (255, 255, 255)])

for i in range(5):
    rect = pygame.Rect(i * 80, 80, 80, 80)
    rects.append([rect, (255, 255, 255)])

for i in range(5):
    rect = pygame.Rect(i * 80, 160, 80, 80)
    rects.append([rect, (255, 255, 255)])

for i in range(5):
    rect = pygame.Rect(i * 80, 240, 80, 80)
    rects.append([rect, (255, 255, 255)])

for i in range(5):
    rect = pygame.Rect(i * 80, 320, 80, 80)
    rects.append([rect, (255, 255, 255)])

#Main loop

#Player one
while drawing:

    while turn1:

        #Quit loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                drawing = False
                turn1 = False

            #If grid pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                
                #Checks first row
                if b <= 5:
                    if x >= (b - 1) * 80 and x <= (b - 1) * 80 + 80:
                        if y >= 0 and y <= 80:
                            rects[b - 1][1] = (0, 255, 0)
                            print("Correct! Player 1 wins!")
                            drawing = False
                            turn1 = False

                            for rect in rects:
                                pygame.draw.rect(window, rect[1], rect[0])
                        
                        else:
                            for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 0 and y <= 80:
                                        rects[i][1] = (255, 0, 0)

                            turn1 = not turn1
                            turn2 = not turn2
                            print("Wrong tile! Player 2's turn!")

                    else:
                        for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 0 and y <= 80:
                                        rects[i][1] = (255, 0, 0)

                        turn1 = not turn1
                        turn2 = not turn2
                        print("Wrong tile! Player 2's turn!")

                else:
                    for i in range(5):
                            if x >= i * 80 and x <= i * 80 + 80:
                                if y >= 0 and y <= 80:
                                    rects[i][1] = (255, 0, 0)
                                            
                #Checks second row
                if b <= 10 and b >= 6:
                    if x >= (b - 6) * 80 and x <= (b - 6) * 80 + 80:
                        if y >= 80 and y <= 1600:
                            rects[b - 1][1] = (0, 255, 0)
                            print("Correct! Player 1 wins!")
                            drawing = False
                            turn1 = False

                            for rect in rects:
                                pygame.draw.rect(window, rect[1], rect[0])
                        
                        else:
                            for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 80 and y <= 160:
                                        rects[i + 5][1] = (255, 0, 0)

                            turn1 = not turn1
                            print("Wrong tile! Player 2's turn!")
                            turn2 = not turn2
                    
                    else:
                        for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 80 and y <= 160:
                                        rects[i + 5][1] = (255, 0, 0)

                        turn1 = not turn1
                        turn2 = not turn2
                        print("Wrong tile! Player 2's turn!")
                
                else:
                    for i in range(5):
                            if x >= i * 80 and x <= i * 80 + 80:
                                if y >= 80 and y <= 160:
                                    rects[i + 5][1] = (255, 0, 0)

                #Checks 3rd row
                if b <= 15 and b >= 11:
                    if x >= (b - 11) * 80 and x <= (b - 11) * 80 + 80:
                        if y >= 160 and y <= 240:
                            rects[b - 1][1] = (0, 255, 0)
                            print("Correct! Player 1 wins!")
                            drawing = False
                            turn1 = False
                            
                            for rect in rects:
                                pygame.draw.rect(window, rect[1], rect[0])

                        else:
                            for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 160 and y <= 240:
                                        rects[i + 10][1] = (255, 0, 0)
                                       
                            turn1 = not turn1
                            print("Wrong tile! Player 2's turn!")
                            turn2 = not turn2

                    else:
                        for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 160 and y <= 240:
                                        rects[i + 10][1] = (255, 0, 0)
                                        
                        turn1 = not turn1
                        turn2 = not turn2
                        print("Wrong tile! Player 2's turn!")

                else:
                    for i in range(5):
                            if x >= i * 80 and x <= i * 80 + 80:
                                if y >= 160 and y <= 240:
                                    rects[i + 10][1] = (255, 0, 0)

                #Checks 4th row
                if b <= 20 and b >= 16:
                    if x >= (b - 16) * 80 and x <= (b - 16) * 80 + 80:
                        if y >= 240 and y <= 320:
                            rects[b - 1][1] = (0, 255, 0)
                            print("Correct! Player 1 wins!")
                            drawing = False
                            turn1 = False

                            for rect in rects:
                                pygame.draw.rect(window, rect[1], rect[0])

                        else:
                            for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 240 and y <= 320:
                                        rects[i + 15][1] = (255, 0, 0)
                                       
                            turn1 = not turn1
                            turn2 = not turn2
                            print("Wrong tile! Player 2's turn!")

                    else:
                        for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 240 and y <= 320:
                                        rects[i + 15][1] = (255, 0, 0)
                                        
                        turn1 = not turn1
                        turn2 = not turn2
                        print("Wrong tile! Player 2's turn!")

                else:
                    for i in range(5):
                            if x >= i * 80 and x <= i * 80 + 80:
                                if y >= 240 and y <= 320:
                                    rects[i + 15][1] = (255, 0, 0)

                #Last row
                if b <= 25 and b >= 21:
                    if (x >= (b - 21) * 80) and (x <= (b - 21) * 80 + 80):
                        print(x)
                        if y >= 320 and y <= 400:
                            rects[b - 1][1] = (0, 255, 0)
                            print("Correct! Player 1 wins!")
                            drawing = False
                            turn1 = False

                            for rect in rects:
                                pygame.draw.rect(window, rect[1], rect[0])


                        else:
                            for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 320 and y <= 400:
                                        rects[i + 20][1] = (255, 0, 0)
                                       
                            turn1 = not turn1
                            print("Wrong tile! Player 2's turn!")
                            turn2 = not turn2

                    else:
                        for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 320 and y <= 400:
                                        rects[i + 20][1] = (255, 0, 0)
                                        
                        turn1 = not turn1
                        turn2 = not turn2
                        print("Wrong tile! Player 2's turn!")

                else:
                    for i in range(5):
                            if x >= i * 80 and x <= i * 80 + 80:
                                if y >= 320 and y <= 400:
                                    rects[i + 20][1] = (255, 0, 0)
        #Drawing
        for rect in rects:
            pygame.draw.rect(window, rect[1], rect[0])
            pygame.draw.rect(window, (0, 0, 0), rect[0], 1)
        
        pygame.display.flip()
        c.tick(30)


    #Player 2
    while turn2:

        #Quit loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                drawing = False
                turn2 = False
            
            #Guess
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                
                #Checks first row
                if a <= 5:
                    if x >= (a - 1) * 80 and x <= (a - 1) * 80 + 80:
                        if y >= 0 and y <= 80:
                            rects[a - 1][1] = (0, 255, 0)
                            print("Correct! Player 2 wins!")
                            drawing = False
                            turn2 = False

                            for rect in rects:
                                pygame.draw.rect(window, rect[1], rect[0])

                        else:
                            for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 0 and y <= 80:
                                        rects[i][1] = (255, 0, 0)
                                       
                            turn2 = not turn2
                            turn1 = not turn1
                            print("Wrong tile! Player 1's turn!")

                    else:
                        for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 0 and y <= 80:
                                        rects[i][1] = (255, 0, 0)
                                        
                        turn2 = not turn2
                        turn1 = not turn1
                        print("Wrong tile! Player 1's turn!")

                else:
                    for i in range(5):
                            if x >= i * 80 and x <= i * 80 + 80:
                                if y >= 0 and y <= 80:
                                    rects[i][1] = (255, 0, 0)

                #Checks 2nd row
                if a <= 10 and a >= 6:
                    if x >= (a - 6) * 80 and x <= (a - 6) * 80 + 80:
                        if y >= 80 and y <= 160:
                            rects[a - 1][1] = (0, 255, 0)
                            print("Correct! Player 2 wins!")
                            drawing = False
                            turn2 = False

                            for rect in rects:
                                pygame.draw.rect(window, rect[1], rect[0])
                        
                        else:
                            for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 80 and y <= 160:
                                        rects[i + 5][1] = (255, 0, 0)
                                       
                            turn2 = not turn2
                            turn1 = not turn1
                            print("Wrong tile! Player 1's turn!")
                    
                    else:
                        for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 80 and y <= 160:
                                        rects[i + 5][1] = (255, 0, 0)
                                        
                        turn2 = not turn2
                        turn1 = not turn1
                        print("Wrong tile! Player 1's turn!")

                else:
                    for i in range(5):
                            if x >= i * 80 and x <= i * 80 + 80:
                                if y >= 80 and y <= 160:
                                    rects[i + 5][1] = (255, 0, 0)

                #Checks 3rd row
                if a <= 15 and a >= 11:
                    if x >= (a - 11) * 80 and x <= (a - 11) * 80 + 80:
                        if y >= 160 and y <= 240:
                            rects[a - 1][1] = (0, 255, 0)
                            print("Correct! Player 2 wins!")
                            drawing = False
                            turn2 = False

                            for rect in rects:
                                pygame.draw.rect(window, rect[1], rect[0])

                        else:
                            for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 160 and y <= 240:
                                        rects[i + 10][1] = (255, 0, 0)
                                        
                            turn2 = not turn2
                            turn1 = not turn1
                            print("Wrong tile! Player 1's Turn!")
                    
                    else:
                        for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 160 and y <= 240:
                                        rects[i + 10][1] = (255, 0, 0)
                                        
                        turn2 = not turn2
                        turn1 = not turn1
                        print("Wrong tile! Player 1's turn!")

                else:
                    for i in range(5):
                            if x >= i * 80 and x <= i * 80 + 80:
                                if y >= 160 and y <= 240:
                                    rects[i + 10][1] = (255, 0, 0)

                #Checks 4th row
                if a <= 20 and a >= 16:
                    if x >= (a - 16) * 80 and x <= (a - 16) * 80 + 80:
                        if y >= 240 and y <= 320:
                            rects[a - 1][1] = (0, 255, 0)
                            print("Correct! Player 2 wins!")
                            drawing = False
                            turn2 = False

                            for rect in rects:
                                pygame.draw.rect(window, rect[1], rect[0])

                        else:
                            for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 240 and y <= 320:
                                        rects[i + 15][1] = (255, 0, 0)
                                        
                            turn2 = not turn2
                            turn1 = not turn1
                            print("Wrong tile! Player 1's turn!")
                    
                    else:
                        for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 240 and y <= 320:
                                        rects[i + 15][1] = (255, 0, 0)
                                        
                        turn2 = not turn2
                        turn1 = not turn1
                        print("Wrong tile! Player 1's turn!")

                else:
                    for i in range(5):
                            if x >= i * 80 and x <= i * 80 + 80:
                                if y >= 240 and y <= 320:
                                    rects[i + 15][1] = (255, 0, 0)

                #Checks last row
                if a <= 25 and a >= 21:
                    if x >= (a - 21) * 80 and x <= (a - 21) * 80 + 80:
                        if y >= 0 and y <= 80:
                            rects[a - 1][1] = (0, 255, 0)
                            print("Correct! Player 2 wins!")
                            drawing = False
                            turn2 = False

                            for rect in rects:
                                pygame.draw.rect(window, rect[1], rect[0])


                        else:
                            for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 320 and y <= 400:
                                        rects[i + 20][1] = (255, 0, 0)
                                        
                            turn2 = not turn2
                            turn1 = not turn1
                            print("Wrong tile! Player 1's turn!")

                    else:
                        for i in range(5):
                                if x >= i * 80 and x <= i * 80 + 80:
                                    if y >= 320 and y <= 400:
                                        rects[i + 20][1] = (255, 0, 0)
                                        
                        turn2 = not turn2
                        turn1 = not turn1
                        print("Wrong tile! Player 1's turn!")

                else:
                    for i in range(5):
                            if x >= i * 80 and x <= i * 80 + 80:
                                if y >= 320 and y <= 400:
                                    rects[i + 20][1] = (255, 0, 0)

        #Drawing 2         
        for rect in rects:
            pygame.draw.rect(window, rect[1], rect[0])
            pygame.draw.rect(window, (0, 0, 0), rect[0], 1)
        
        pygame.display.flip()
        c.tick(30)