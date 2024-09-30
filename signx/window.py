import pygame, threading

class SignatureWindow:
    def __init__(self):
        self.fps = 300
        
        self.window_size = (800, 800)
        self.canvas_size = (800, 800)
        
        self.screen = None
        self.canvas = None
        
        self.brush_size = 3
        
        self.loop_thread = None
        
        self._finished = False
        
        #[x, y, velocity]
        self.sig_buffer = []
        
        self.keep_running = True
        
        self.last_coords = None
        
    def run(self):
        self.loop_thread = threading.Thread(target=self._loop)
        self.loop_thread.start()
        
    def stop(self):
        self.keep_running = False
        
    def get_data(self):
        return self.canvas
    
    def reset(self):
        """_summary_
        Reset the signature window to its initial state.
        """
        
        self.canvas.fill((255, 255, 255))
        self._finished = False
        self.sig_buffer = []
        
    def finished(self):
        return self._finished
    
    def get_signature(self):
        return self.sig_buffer
    
    def running(self):
        return self.keep_running
        
    def _draw_canvas(self):
        x, y = self.screen.get_size()
        self.screen.blit(self.canvas, [x/2 - self.canvas_size[0]/2, y/2 - self.canvas_size[1]/2])
        
    def _draw_signature(self):
        """_summary_
        Draw the signature on the canvas.
        Returns:
            bool: Returns True if the signature is being drawn.
        """
        
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            
            dx = mx - self.window_size[0]/2 + self.canvas_size[0]/2
            dy = my - self.window_size[1]/2 + self.canvas_size[1]/2
            
            pygame.draw.circle(
                self.canvas,
                (0, 0, 0),
                [dx, dy],
                self.brush_size,
            )
            
            if self.last_coords is None:
                self.last_coords = (dx, dy)
            self.sig_buffer.append((dx, dy, (dx - self.last_coords[0], dy - self.last_coords[1])))
            self.last_coords = (dx, dy)
            return True
        return False
            
    def _check_drawn(self):
        """_summary_
        Check if the signature has been drawn.
        Returns:
            bool: Returns True if the signature has been drawn.
        """
        
        for x in range(self.canvas_size[0]):
            for y in range(self.canvas_size[1]):
                if self.canvas.get_at((x, y)) == (0, 0, 0, 255):
                    return True
        return False
        
    def _loop(self):
        """_summary_
        The main loop of the signature window.
        """
        
        pygame.init()
        
        self.screen = pygame.display.set_mode(self.window_size)
        self.canvas = pygame.Surface(self.canvas_size)
        
        self.canvas.fill((255, 255, 255))
        
        while self.keep_running:
            self.screen.fill((30, 30, 30))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self._draw_canvas()
            if not self._draw_signature():
                if self._check_drawn():
                    self._finished = True
            
            pygame.display.update()
            pygame.time.Clock().tick(self.fps)
            
    def __repr__(self):
        return f"<SignatureWindow finished={self.finished()}>"