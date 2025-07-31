import tkinter as tk
import math
import time
import random

class LuxuryModernClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Luxury Modern Decorative Clock")
        self.root.geometry("700x800")
        self.root.configure(bg='#1a1a1a')
        
        # Create canvas for the clock
        self.canvas = tk.Canvas(root, width=680, height=750, bg='#1a1a1a', highlightthickness=0)
        self.canvas.pack(pady=25)
        
        # Clock parameters
        self.center_x = 340
        self.center_y = 375
        self.main_clock_radius = 110
        
        # Animation variables
        self.glow_intensity = 0
        self.glow_direction = 1
        
        self.draw_background()
        self.draw_decorative_framework()
        self.draw_ornamental_elements()
        self.draw_clock_face()
        self.animate_glow()
        self.update_clock()
    
    def create_gradient_oval(self, x1, y1, x2, y2, color1, color2, steps=15):
        """Create gradient effect for ovals"""
        width = x2 - x1
        height = y2 - y1
        for i in range(steps):
            ratio = i / steps
            # Color interpolation
            r1, g1, b1 = self.hex_to_rgb(color1)
            r2, g2, b2 = self.hex_to_rgb(color2)
            
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)
            
            color = f"#{r:02x}{g:02x}{b:02x}"
            
            scale = 1 - ratio * 0.8
            new_width = width * scale
            new_height = height * scale
            offset_x = (width - new_width) / 2
            offset_y = (height - new_height) / 2
            
            self.canvas.create_oval(
                x1 + offset_x, y1 + offset_y,
                x1 + offset_x + new_width, y1 + offset_y + new_height,
                fill=color, outline=""
            )
    
    def hex_to_rgb(self, hex_color):
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def draw_background(self):
        """Draw sophisticated background with subtle patterns"""
        # Main background
        self.canvas.create_rectangle(0, 0, 680, 750, fill='#2a2a2a', outline='')
        
        # Subtle radial gradient background
        for i in range(20):
            radius = 400 - i * 15
            alpha = 0.02 + i * 0.001
            gray_val = int(42 + i * 2)
            color = f"#{gray_val:02x}{gray_val:02x}{gray_val:02x}"
            
            self.canvas.create_oval(
                self.center_x - radius, self.center_y - radius,
                self.center_x + radius, self.center_y + radius,
                fill=color, outline=""
            )
    
    def draw_decorative_framework(self):
        """Draw the main geometric framework"""
        grid_color = '#DAA520'
        accent_color = '#FFD700'
        
        # Main outer rings with multiple layers
        for i, (radius, width, color) in enumerate([
            (220, 6, accent_color),
            (215, 2, grid_color),
            (200, 4, grid_color),
            (195, 1, accent_color)
        ]):
            self.canvas.create_oval(
                self.center_x - radius, self.center_y - radius,
                self.center_x + radius, self.center_y + radius,
                outline=color, width=width, fill=""
            )
        
        # Enhanced geometric grid with varying thickness
        line_sets = [
            # Main grid lines
            {'spacing': 80, 'width': 3, 'color': grid_color, 'length': 440},
            # Secondary grid lines
            {'spacing': 40, 'width': 1, 'color': '#B8860B', 'length': 300},
            # Fine detail lines
            {'spacing': 20, 'width': 1, 'color': '#8B7355', 'length': 200, 'alpha': 0.5}
        ]
        
        for line_set in line_sets:
            spacing = line_set['spacing']
            width = line_set['width']
            color = line_set['color']
            length = line_set['length']
            
            # Horizontal lines
            for i in range(-4, 5):
                y_pos = self.center_y + i * spacing
                if abs(i * spacing) <= length // 2:
                    self.canvas.create_line(
                        self.center_x - length//2, y_pos,
                        self.center_x + length//2, y_pos,
                        fill=color, width=width
                    )
            
            # Vertical lines
            for i in range(-5, 6):
                x_pos = self.center_x + i * spacing
                if abs(i * spacing) <= length // 2:
                    self.canvas.create_line(
                        x_pos, self.center_y - length//2,
                        x_pos, self.center_y + length//2,
                        fill=color, width=width
                    )
        
        # Diagonal accent lines
        for angle in [45, 135, 225, 315]:
            for radius in [150, 180]:
                angle_rad = math.radians(angle)
                start_x = self.center_x + (radius - 30) * math.cos(angle_rad)
                start_y = self.center_y + (radius - 30) * math.sin(angle_rad)
                end_x = self.center_x + radius * math.cos(angle_rad)
                end_y = self.center_y + radius * math.sin(angle_rad)
                
                self.canvas.create_line(
                    start_x, start_y, end_x, end_y,
                    fill=accent_color, width=2
                )
    
    def draw_luxury_sunburst(self, x, y, radius, color, num_rays=32):
        """Enhanced sunburst pattern with multiple layers"""
        # Outer glow effect
        for i in range(5):
            glow_radius = radius + i * 3
            glow_alpha = 0.3 - i * 0.05
            self.canvas.create_oval(
                x - glow_radius, y - glow_radius,
                x + glow_radius, y + glow_radius,
                fill="", outline=color, width=1
            )
        
        # Main circle with gradient
        self.create_gradient_oval(
            x - radius, y - radius, x + radius, y + radius,
            color, '#8B7355'
        )
        
        # Radiating rays with varying lengths
        for i in range(num_rays):
            angle = i * (360 / num_rays)
            angle_rad = math.radians(angle)
            
            # Alternating ray lengths for more sophisticated look
            if i % 4 == 0:
                inner_radius = radius * 0.2
                outer_radius = radius * 0.95
                width = 2
            elif i % 2 == 0:
                inner_radius = radius * 0.3
                outer_radius = radius * 0.85
                width = 1
            else:
                inner_radius = radius * 0.4
                outer_radius = radius * 0.75
                width = 1
            
            inner_x = x + inner_radius * math.cos(angle_rad)
            inner_y = y + inner_radius * math.sin(angle_rad)
            outer_x = x + outer_radius * math.cos(angle_rad)
            outer_y = y + outer_radius * math.sin(angle_rad)
            
            self.canvas.create_line(
                inner_x, inner_y, outer_x, outer_y,
                fill='#DAA520', width=width
            )
        
        # Central jewel-like element
        for i in range(3):
            jewel_radius = 8 - i * 2
            jewel_color = ['#FFD700', '#DAA520', '#B8860B'][i]
            self.canvas.create_oval(
                x - jewel_radius, y - jewel_radius,
                x + jewel_radius, y + jewel_radius,
                fill=jewel_color, outline=""
            )
    
    def draw_ornamental_elements(self):
        """Draw enhanced decorative elements"""
        # Large decorative sunburst circles
        sunburst_positions = [
            (self.center_x - 140, self.center_y - 100, 35),  # Top left
            (self.center_x + 120, self.center_y - 120, 40),  # Top right  
            (self.center_x - 150, self.center_y + 140, 30),  # Bottom left
            (self.center_x + 100, self.center_y + 160, 38),  # Bottom right
            (self.center_x - 50, self.center_y - 180, 25),   # Top center
        ]
        
        for x, y, radius in sunburst_positions:
            self.draw_luxury_sunburst(x, y, radius, '#F4E4BC')
        
        # Sophisticated black spheres with metallic edges
        black_positions = [
            (self.center_x - 80, self.center_y - 160, 18),
            (self.center_x + 160, self.center_y - 60, 22),
            (self.center_x - 170, self.center_y + 80, 16),
            (self.center_x + 140, self.center_y + 100, 20),
            (self.center_x - 100, self.center_y + 200, 17),
            (self.center_x + 60, self.center_y + 220, 14),
            (self.center_x + 200, self.center_y + 20, 12),
            (self.center_x - 200, self.center_y - 40, 15),
        ]
        
        for x, y, radius in black_positions:
            # Outer glow
            self.canvas.create_oval(
                x - radius - 3, y - radius - 3,
                x + radius + 3, y + radius + 3,
                fill="", outline='#444', width=1
            )
            
            # Main sphere with gradient effect
            self.create_gradient_oval(
                x - radius, y - radius, x + radius, y + radius,
                '#1a1a1a', '#000000'
            )
            
            # Metallic highlight
            highlight_x = x - radius * 0.3
            highlight_y = y - radius * 0.3
            highlight_radius = radius * 0.3
            self.canvas.create_oval(
                highlight_x - highlight_radius, highlight_y - highlight_radius,
                highlight_x + highlight_radius, highlight_y + highlight_radius,
                fill='#333', outline=""
            )
        
        # Floating golden accent elements
        golden_accents = [
            (self.center_x + 180, self.center_y + 40, 10, 'circle'),
            (self.center_x - 190, self.center_y - 20, 8, 'circle'),
            (self.center_x + 20, self.center_y + 240, 15, 'circle'),
            (self.center_x - 20, self.center_y - 240, 12, 'diamond'),
            (self.center_x + 220, self.center_y - 100, 6, 'star'),
        ]
        
        for x, y, size, shape in golden_accents:
            if shape == 'circle':
                self.create_gradient_oval(
                    x - size, y - size, x + size, y + size,
                    '#FFD700', '#DAA520'
                )
            elif shape == 'diamond':
                points = [x, y-size, x+size, y, x, y+size, x-size, y]
                self.canvas.create_polygon(points, fill='#FFD700', outline='#DAA520', width=2)
            elif shape == 'star':
                self.draw_star(x, y, size, '#FFD700')
    
    def draw_star(self, x, y, size, color):
        """Draw a decorative star"""
        points = []
        for i in range(10):  # 5-pointed star = 10 points
            angle = i * math.pi / 5
            if i % 2 == 0:
                radius = size
            else:
                radius = size * 0.4
            
            px = x + radius * math.cos(angle - math.pi/2)
            py = y + radius * math.sin(angle - math.pi/2)
            points.extend([px, py])
        
        self.canvas.create_polygon(points, fill=color, outline='#B8860B', width=1)
    
    def draw_clock_face(self):
        """Draw enhanced clock face with luxury styling"""
        # Multiple layered clock backgrounds
        layers = [
            (self.main_clock_radius + 20, '#DAA520', 4),  # Outer golden ring
            (self.main_clock_radius + 15, '#FFD700', 2),  # Middle accent
            (self.main_clock_radius + 10, '#F5F5DC', 0),  # Outer background
            (self.main_clock_radius, '#FFF8DC', 0),       # Main background
        ]
        
        for radius, color, width in layers:
            if width > 0:
                self.canvas.create_oval(
                    self.center_x - radius, self.center_y - radius,
                    self.center_x + radius, self.center_y + radius,
                    outline=color, width=width, fill=""
                )
            else:
                self.create_gradient_oval(
                    self.center_x - radius, self.center_y - radius,
                    self.center_x + radius, self.center_y + radius,
                    color, '#E6D7B8'
                )
        
        # Luxury inner pattern
        inner_radius = self.main_clock_radius - 35
        self.canvas.create_oval(
            self.center_x - inner_radius, self.center_y - inner_radius,
            self.center_x + inner_radius, self.center_y + inner_radius,
            fill="", outline='#DAA520', width=1
        )
        
        # Enhanced hour numbers with better typography
        for i in range(1, 13):
            angle = math.radians(i * 30 - 90)
            
            # Calculate position for numbers
            num_x = self.center_x + (self.main_clock_radius - 30) * math.cos(angle)
            num_y = self.center_y + (self.main_clock_radius - 30) * math.sin(angle)
            
            # Number background circle
            self.canvas.create_oval(
                num_x - 12, num_y - 12, num_x + 12, num_y + 12,
                fill='#F0F0F0', outline='#DAA520', width=1
            )
            
            # Draw hour numbers
            self.canvas.create_text(
                num_x, num_y, text=str(i),
                font=('Georgia', 14, 'bold'), fill='#2a2a2a'
            )
        
        # Enhanced minute and hour marks
        for i in range(60):
            angle = math.radians(i * 6 - 90)
            if i % 15 == 0:  # Quarter hour marks
                inner_radius = self.main_clock_radius - 20
                outer_radius = self.main_clock_radius - 5
                width = 4
                color = '#DAA520'
            elif i % 5 == 0:  # Hour marks
                inner_radius = self.main_clock_radius - 18
                outer_radius = self.main_clock_radius - 5
                width = 3
                color = '#2a2a2a'
            else:  # Minute marks
                inner_radius = self.main_clock_radius - 12
                outer_radius = self.main_clock_radius - 5
                width = 1
                color = '#666'
            
            inner_x = self.center_x + inner_radius * math.cos(angle)
            inner_y = self.center_y + inner_radius * math.sin(angle)
            outer_x = self.center_x + outer_radius * math.cos(angle)
            outer_y = self.center_y + outer_radius * math.sin(angle)
            
            self.canvas.create_line(
                inner_x, inner_y, outer_x, outer_y,
                width=width, fill=color, capstyle=tk.ROUND
            )
        
        # Luxury center hub with multiple layers
        hub_layers = [
            (15, '#DAA520', '#FFD700'),
            (12, '#B8860B', '#DAA520'),
            (8, '#8B7355', '#B8860B'),
            (4, '#FFD700', '#FFF8DC')
        ]
        
        for radius, outer_color, inner_color in hub_layers:
            self.create_gradient_oval(
                self.center_x - radius, self.center_y - radius,
                self.center_x + radius, self.center_y + radius,
                outer_color, inner_color
            )
    
    def draw_luxury_hand(self, angle, length, width, color, hand_type, tag):
        """Draw sophisticated clock hands with luxury styling"""
        angle_rad = math.radians(angle - 90)
        end_x = self.center_x + length * math.cos(angle_rad)
        end_y = self.center_y + length * math.sin(angle_rad)
        
        if hand_type == 'second':
            # Elegant second hand with counterweight
            # Main hand
            self.canvas.create_line(
                self.center_x, self.center_y, end_x, end_y,
                width=width, fill=color, capstyle=tk.ROUND, tags=tag
            )
            # Counterweight
            counter_x = self.center_x - 20 * math.cos(angle_rad)
            counter_y = self.center_y - 20 * math.sin(angle_rad)
            self.canvas.create_line(
                self.center_x, self.center_y, counter_x, counter_y,
                width=width+1, fill=color, capstyle=tk.ROUND, tags=tag
            )
            # Second hand tip circle
            self.canvas.create_oval(
                end_x - 3, end_y - 3, end_x + 3, end_y + 3,
                fill=color, outline="", tags=tag
            )
        else:
            # Luxury minute and hour hands with tapered design
            perp_angle = angle_rad + math.pi/2
            
            # Create elegant hand shape
            base_width = width
            mid_width = width * 0.7
            tip_width = width * 0.3
            
            # Base points
            base_offset = base_width / 2
            base_x1 = self.center_x + base_offset * math.cos(perp_angle)
            base_y1 = self.center_y + base_offset * math.sin(perp_angle)
            base_x2 = self.center_x - base_offset * math.cos(perp_angle)
            base_y2 = self.center_y - base_offset * math.sin(perp_angle)
            
            # Mid points (70% along the hand)
            mid_ratio = 0.7
            mid_x = self.center_x + length * mid_ratio * math.cos(angle_rad)
            mid_y = self.center_y + length * mid_ratio * math.sin(angle_rad)
            mid_offset = mid_width / 2
            mid_x1 = mid_x + mid_offset * math.cos(perp_angle)
            mid_y1 = mid_y + mid_offset * math.sin(perp_angle)
            mid_x2 = mid_x - mid_offset * math.cos(perp_angle)
            mid_y2 = mid_y - mid_offset * math.sin(perp_angle)
            
            # Tip point
            tip_offset = tip_width / 2
            tip_x1 = end_x + tip_offset * math.cos(perp_angle)
            tip_y1 = end_y + tip_offset * math.sin(perp_angle)
            tip_x2 = end_x - tip_offset * math.cos(perp_angle)
            tip_y2 = end_y - tip_offset * math.sin(perp_angle)
            
            # Create hand polygon
            points = [
                base_x1, base_y1,
                mid_x1, mid_y1,
                tip_x1, tip_y1,
                end_x, end_y,
                tip_x2, tip_y2,
                mid_x2, mid_y2,
                base_x2, base_y2
            ]
            
            # Main hand body
            self.canvas.create_polygon(
                points, fill=color, outline='#1a1a1a', width=1,
                smooth=True, tags=tag
            )
            
            # Hand highlight
            highlight_color = '#666' if color == '#2a2a2a' else '#FF6B6B'
            highlight_points = [
                base_x1, base_y1,
                mid_x1, mid_y1,
                end_x, end_y,
                mid_x2, mid_y2
            ]
            self.canvas.create_polygon(
                highlight_points, fill="", outline=highlight_color, width=1,
                smooth=True, tags=tag
            )
    
    def animate_glow(self):
        """Animate subtle glow effects"""
        self.glow_intensity += self.glow_direction * 5
        if self.glow_intensity >= 30:
            self.glow_direction = -1
        elif self.glow_intensity <= 0:
            self.glow_direction = 1
        
        # Update glow effects on decorative elements
        self.root.after(100, self.animate_glow)
    
    def update_clock(self):
        """Update clock with enhanced animations"""
        # Clear previous hands
        self.canvas.delete("hands")
        
        # Get current time
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec
        
        # Calculate angles with smooth movement
        second_angle = seconds * 6 + (time.time() % 1) * 6  # Smooth second movement
        minute_angle = minutes * 6 + seconds * 0.1
        hour_angle = hours * 30 + minutes * 0.5
        
        # Draw hands with luxury styling
        self.draw_luxury_hand(second_angle, 85, 2, '#DC143C', 'second', "hands")
        self.draw_luxury_hand(minute_angle, 75, 5, '#2a2a2a', 'minute', "hands")
        self.draw_luxury_hand(hour_angle, 55, 7, '#2a2a2a', 'hour', "hands")
        
        # Enhanced digital time display
        time_str = time.strftime("%H:%M:%S", current_time)
        date_str = time.strftime("%A, %B %d, %Y", current_time)
        
        # Clear previous display
        self.canvas.delete("time_display")
        
        # Luxury time display box
        box_width = 260
        box_height = 60
        box_x = self.center_x - box_width//2
        box_y = 650
        
        # Background with gradient effect
        self.create_gradient_oval(
            box_x, box_y, box_x + box_width, box_y + box_height,
            '#1a1a1a', '#333333'
        )
        
        # Border
        self.canvas.create_rectangle(
            box_x, box_y, box_x + box_width, box_y + box_height,
            fill="", outline='#DAA520', width=2, tags="time_display"
        )
        
        # Time text with shadow effect
        shadow_offset = 2
        # Shadow
        self.canvas.create_text(
            self.center_x + shadow_offset, box_y + 20 + shadow_offset,
            text=time_str, font=('Georgia', 16, 'bold'),
            fill='#000', tags="time_display"
        )
        # Main text
        self.canvas.create_text(
            self.center_x, box_y + 20, text=time_str,
            font=('Georgia', 16, 'bold'), fill='#FFD700', tags="time_display"
        )
        
        # Date text
        self.canvas.create_text(
            self.center_x, box_y + 45, text=date_str,
            font=('Georgia', 11), fill='#F5F5DC', tags="time_display"
        )
        
        # Schedule next update (smoother at 50ms intervals)
        self.root.after(50, self.update_clock)

def main():
    root = tk.Tk()
    clock = LuxuryModernClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()