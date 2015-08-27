import pygame

pygame.init()

levels = [  [ pygame.Rect(0, 0, 600, 20), #level 1   border
              pygame.Rect(0, 0, 20, 600),
              pygame.Rect(580, 0, 20, 600),
              pygame.Rect(0, 580, 600, 20),
              pygame.Rect(300, 100, 120, 20), #horiz
              pygame.Rect(0, 260, 500, 20),
              pygame.Rect(0, 400, 140, 20),
              pygame.Rect(180, 400, 40, 20),
              pygame.Rect(380, 480, 220, 20),
              pygame.Rect(400, 100, 20, 160), #vert
              pygame.Rect(380, 260, 20, 100),
              pygame.Rect(200, 400, 20, 200),
              pygame.Rect(380, 400, 20, 100),
              pygame.Rect(420, 480, 20, 100) ],
            
            [ pygame.Rect(0, 0, 600, 20), #level 2   borders
              pygame.Rect(0, 0, 20, 600),
              pygame.Rect(580, 0, 20, 600),
              pygame.Rect(0, 580, 600, 20),
              pygame.Rect(300, 100, 120, 20), #horiz
              pygame.Rect(0, 260, 500, 20),
              pygame.Rect(0, 400, 119, 20),
              pygame.Rect(161, 400, 59, 20),
              pygame.Rect(380, 480, 220, 20),
              pygame.Rect(0, 520, 80, 20),
              pygame.Rect(400, 100, 20, 160), #vert
              pygame.Rect(260, 260, 20, 119),
              pygame.Rect(320, 260, 20, 290),
              pygame.Rect(260, 401, 20, 199),
              pygame.Rect(380, 260, 20, 100),
              pygame.Rect(200, 400, 20, 200),
              pygame.Rect(380, 400, 20, 100),
              pygame.Rect(420, 480, 20, 100),
              pygame.Rect(60, 520, 20, 38) ],

            [ pygame.Rect(0, 0, 600, 20), #level 3   borders
              pygame.Rect(0, 0, 20, 600),
              pygame.Rect(580, 0, 20, 600),
              pygame.Rect(0, 580, 600, 20),
              pygame.Rect(300, 100, 120, 20), #horiz
              pygame.Rect(0, 260, 500, 20),
              pygame.Rect(0, 400, 119, 20),
              pygame.Rect(161, 400, 59, 20),
              pygame.Rect(380, 480, 220, 20),
              pygame.Rect(0, 520, 80, 20),
              pygame.Rect(400, 100, 20, 160), #vert
              pygame.Rect(260, 260, 20, 119),
              pygame.Rect(320, 260, 20, 290),
              pygame.Rect(260, 401, 20, 199),
              pygame.Rect(380, 260, 20, 100),
              pygame.Rect(200, 400, 20, 200),
              pygame.Rect(380, 400, 20, 100),
              pygame.Rect(420, 480, 20, 100),
              pygame.Rect(60, 520, 20, 38) ],
            
            [ pygame.Rect(0, 0, 600, 20), #level 4   borders
              pygame.Rect(0, 0, 20, 600),
              pygame.Rect(580, 0, 20, 600),
              pygame.Rect(0, 580, 600, 20),
              pygame.Rect(300, 100, 120, 160), #horiz
              pygame.Rect(0, 260, 500, 20),
              pygame.Rect(0, 400, 100, 20),
              pygame.Rect(0, 420, 80, 20),
              pygame.Rect(0, 440, 60, 20),
              pygame.Rect(0, 460, 40, 20),
              pygame.Rect(160, 420, 40, 20),
              pygame.Rect(180, 440, 20, 20),
              pygame.Rect(160, 400, 60, 20),
              pygame.Rect(380, 480, 220, 20),
              pygame.Rect(320, 520, 220, 20),
              pygame.Rect(0, 520, 80, 20),
              pygame.Rect(260, 260, 20, 110), #vert
              pygame.Rect(320, 260, 20, 280),
              pygame.Rect(260, 400, 20, 200),
              pygame.Rect(380, 260, 20, 100),
              pygame.Rect(200, 400, 20, 200),
              pygame.Rect(380, 400, 20, 100),
              pygame.Rect(60, 520, 20, 30) ] ]

               
                 
                
