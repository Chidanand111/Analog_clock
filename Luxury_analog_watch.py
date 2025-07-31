import tkinter as tk
import math
import time
from datetime import datetime

class LuxuryWatchClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Luxury Watch-Style Clock")
        self.root.geometry("600x800")
        self.root.configure(bg='#f0f0f0')
        
        # Create canvas for the watch
        self.canvas = tk.Canvas(root, width=580, height=750, bg='#f0f0f0', highlightthickness=0)
        self.canvas.pack(pady=25)
        
        # Watch parameters
        self.center_x = 290
        self.center_y = 375
        self.case_radius = 180
        self.dial_radius = 140
        self.bezel_radius = 165
        
        # Animation
        self.bezel_rotation = 0
        
        self.draw_watch_case()
        self.draw_rotating_bezel()
        self.draw_watch_dial()
        self.draw_crown_and_bracelet()
        self.update_watch()
    
    def create_metallic_gradient(self, x1, y1, x2, y2, metal_type='steel', steps=20):
        """Create metallic gradient effects"""
        colors = {
            'steel': ['#E8E8E8', '#C0C0C0', '#A8A8A8', '#D3D3D3', '#F5F5F5'],
            'gold': ['#FFD700', '#FFC107', '#DAA520', '#F4E157', '#FFF8DC'],
            'blue': ['#1E3A8A', '#2563EB', '#3B82F6', '#60A5FA', '#93C5FD']
        }
        
        color_set = colors[metal_type]
        width = x2 - x1
        height = y2 - y1
        
        for i in range(steps):
            ratio = i / steps
            color_idx = int(ratio * (len(color_set) - 1))
            color = color_set[color_idx]
            
            scale = 1 - ratio * 0.3
            new_width = width * scale
            new_height = height * scale
            offset_x = (width - new_width) / 2
            offset_y = (height - new_height) / 2
            
            self.canvas.create_oval(
                x1 + offset_x, y1 + offset_y,
                x1 + offset_x + new_width, y1 + offset_y + new_height,
                fill=color, outline=""
            )
    
    def draw_watch_case(self):
        """Draw the main watch case with bracelet"""
        # Case shadow
        shadow_offset = 8
        self.canvas.create_oval(
            self.center_x - self.case_radius + shadow_offset,
            self.center_y - self.case_radius + shadow_offset,
            self.center_x + self.case_radius + shadow_offset,
            self.center_y + self.case_radius + shadow_offset,
            fill='#888888', outline='', stipple='gray50'
        )
        
        # Main case body with steel gradient
        self.create_metallic_gradient(
            self.center_x - self.case_radius, self.center_y - self.case_radius,
            self.center_x + self.case_radius, self.center_y + self.case_radius,
            'steel'
        )
        
        # Case edge highlight
        self.canvas.create_oval(
            self.center_x - self.case_radius, self.center_y - self.case_radius,
            self.center_x + self.case_radius, self.center_y + self.case_radius,
            fill='', outline='#FFFFFF', width=3
        )
        
        # Inner case ring
        inner_case_radius = self.case_radius - 15
        self.canvas.create_oval(
            self.center_x - inner_case_radius, self.center_y - inner_case_radius,
            self.center_x + inner_case_radius, self.center_y + inner_case_radius,
            fill='', outline='#A0A0A0', width=2
        )
    
    def draw_rotating_bezel(self):
        """Draw the iconic rotating diving bezel"""
        # Bezel shadow
        self.canvas.create_oval(
            self.center_x - self.bezel_radius - 3, self.center_y - self.bezel_radius - 3,
            self.center_x + self.bezel_radius + 3, self.center_y + self.bezel_radius + 3,
            fill='#333333', outline=''
        )
        
        # Main bezel with blue gradient
        self.create_metallic_gradient(
            self.center_x - self.bezel_radius, self.center_y - self.bezel_radius,
            self.center_x + self.bezel_radius, self.center_y + self.bezel_radius,
            'blue'
        )
        
        # Bezel markings and numbers
        bezel_numbers = [10, 20, 30, 40, 50]
        triangle_at_12 = True
        
        for i in range(60):
            angle = math.radians(i * 6 - 90 + self.bezel_rotation)
            
            if i == 0 and triangle_at_12:
                # Triangle marker at 12 o'clock
                triangle_size = 8
                marker_radius = self.bezel_radius - 15
                marker_x = self.center_x + marker_radius * math.cos(angle)
                marker_y = self.center_y + marker_radius * math.sin(angle)
                
                # Create triangle points
                points = []
                for j in range(3):
                    tri_angle = angle + j * 2 * math.pi / 3
                    px = marker_x + triangle_size * math.cos(tri_angle)
                    py = marker_y + triangle_size * math.sin(tri_angle)
                    points.extend([px, py])
                
                self.canvas.create_polygon(points, fill='#FFD700', outline='#DAA520', width=1)
                
            elif i % 5 == 0:  # Major markers every 5 minutes
                outer_radius = self.bezel_radius - 8
                inner_radius = self.bezel_radius - 25
                
                outer_x = self.center_x + outer_radius * math.cos(angle)
                outer_y = self.center_y + outer_radius * math.sin(angle)
                inner_x = self.center_x + inner_radius * math.cos(angle)
                inner_y = self.center_y + inner_radius * math.sin(angle)
                
                self.canvas.create_line(
                    outer_x, outer_y, inner_x, inner_y,
                    width=3, fill='#FFD700', capstyle=tk.ROUND
                )
                
                # Add numbers for major markers
                minute_value = i
                if minute_value in [10, 20, 30, 40, 50]:
                    num_radius = self.bezel_radius - 35
                    num_x = self.center_x + num_radius * math.cos(angle)
                    num_y = self.center_y + num_radius * math.sin(angle)
                    
                    self.canvas.create_text(
                        num_x, num_y, text=str(minute_value),
                        font=('Arial', 12, 'bold'), fill='#FFD700'
                    )
            
            elif i % 1 == 0:  # Minor markers every minute
                outer_radius = self.bezel_radius - 10
                inner_radius = self.bezel_radius - 20
                
                outer_x = self.center_x + outer_radius * math.cos(angle)
                outer_y = self.center_y + outer_radius * math.sin(angle)
                inner_x = self.center_x + inner_radius * math.cos(angle)
                inner_y = self.center_y + inner_radius * math.sin(angle)
                
                self.canvas.create_line(
                    outer_x, outer_y, inner_x, inner_y,
                    width=1, fill='#E0E0E0'
                )
        
        # Bezel edge serrations
        for i in range(120):  # 120 serrations around the bezel
            angle = math.radians(i * 3)
            outer_radius = self.bezel_radius + 2
            inner_radius = self.bezel_radius - 2
            
            outer_x = self.center_x + outer_radius * math.cos(angle)
            outer_y = self.center_y + outer_radius * math.sin(angle)
            inner_x = self.center_x + inner_radius * math.cos(angle)
            inner_y = self.center_y + inner_radius * math.sin(angle)
            
            self.canvas.create_line(
                outer_x, outer_y, inner_x, inner_y,
                width=1, fill='#666666'
            )
    
    def draw_watch_dial(self):
        """Draw the main watch dial"""
        # Dial shadow/depth
        self.canvas.create_oval(
            self.center_x - self.dial_radius - 5, self.center_y - self.dial_radius - 5,
            self.center_x + self.dial_radius + 5, self.center_y + self.dial_radius + 5,
            fill='#1a1a2e', outline=''
        )
        
        # Main dial with blue gradient
        self.create_metallic_gradient(
            self.center_x - self.dial_radius, self.center_y - self.dial_radius,
            self.center_x + self.dial_radius, self.center_y + self.dial_radius,
            'blue'
        )
        
        # Dial edge ring
        self.canvas.create_oval(
            self.center_x - self.dial_radius, self.center_y - self.dial_radius,
            self.center_x + self.dial_radius, self.center_y + self.dial_radius,
            fill='', outline='#C0C0C0', width=2
        )
        
        # Hour markers
        for i in range(12):
            angle = math.radians(i * 30 - 90)
            
            if i == 0:  # 12 o'clock triangle
                triangle_size = 12
                marker_radius = self.dial_radius - 25
                marker_x = self.center_x + marker_radius * math.cos(angle)
                marker_y = self.center_y + marker_radius * math.sin(angle)
                
                # White triangle with gold outline
                points = [
                    marker_x, marker_y - triangle_size,
                    marker_x - triangle_size * 0.8, marker_y + triangle_size * 0.5,
                    marker_x + triangle_size * 0.8, marker_y + triangle_size * 0.5
                ]
                self.canvas.create_polygon(points, fill='white', outline='#FFD700', width=2)
                
            elif i in [2, 4, 7, 8, 10]:  # Dot markers
                dot_radius = self.dial_radius - 25
                dot_x = self.center_x + dot_radius * math.cos(angle)
                dot_y = self.center_y + dot_radius * math.sin(angle)
                
                # White dot with gold rim
                self.canvas.create_oval(
                    dot_x - 8, dot_y - 8, dot_x + 8, dot_y + 8,
                    fill='white', outline='#FFD700', width=2
                )
                
            else:  # Rectangle markers for 3, 6, 9
                rect_outer = self.dial_radius - 20
                rect_inner = self.dial_radius - 35
                
                outer_x = self.center_x + rect_outer * math.cos(angle)
                outer_y = self.center_y + rect_outer * math.sin(angle)
                inner_x = self.center_x + rect_inner * math.cos(angle)
                inner_y = self.center_y + rect_inner * math.sin(angle)
                
                # Calculate rectangle corners
                perp_angle = angle + math.pi/2
                width = 6
                
                corners = [
                    outer_x + width * math.cos(perp_angle),
                    outer_y + width * math.sin(perp_angle),
                    outer_x - width * math.cos(perp_angle),
                    outer_y - width * math.sin(perp_angle),
                    inner_x - width * math.cos(perp_angle),
                    inner_y - width * math.sin(perp_angle),
                    inner_x + width * math.cos(perp_angle),
                    inner_y + width * math.sin(perp_angle)
                ]
                
                self.canvas.create_polygon(corners, fill='white', outline='#FFD700', width=1)
        
        # Brand text and model
        self.canvas.create_text(
            self.center_x, self.center_y - 50, text="ROLEX",
            font=('Times', 14, 'bold'), fill='white'
        )
        
        
        # Date window
        date_x = self.center_x + 45
        date_y = self.center_y
        
        # Date window background
        self.canvas.create_rectangle(
            date_x - 15, date_y - 12, date_x + 15, date_y + 12,
            fill='white', outline='#C0C0C0', width=2
        )
        
        # Magnifying cyclops effect
        self.canvas.create_rectangle(
            date_x - 18, date_y - 15, date_x + 18, date_y + 15,
            fill='', outline='#E0E0E0', width=1
        )
        
        # Current date
        current_date = datetime.now()
        date_text = str(current_date.day)
        self.canvas.create_text(
            date_x, date_y, text=date_text,
            font=('Arial', 16, 'bold'), fill='black'
        )
    
    def draw_crown_and_bracelet(self):
        """Draw the crown and bracelet elements"""
        
    def draw_luxury_hands(self, angle, length, width, color, hand_type, tag):
        """Draw luxury watch hands with Mercedes-style design"""
        angle_rad = math.radians(angle - 90)
        end_x = self.center_x + length * math.cos(angle_rad)
        end_y = self.center_y + length * math.sin(angle_rad)
        
        if hand_type == 'hour':
            # Mercedes-style hour hand
            # Main shaft
            perp_angle = angle_rad + math.pi/2
            shaft_width = width
            
            shaft_points = [
                self.center_x + shaft_width//2 * math.cos(perp_angle),
                self.center_y + shaft_width//2 * math.sin(perp_angle),
                self.center_x - shaft_width//2 * math.cos(perp_angle),
                self.center_y - shaft_width//2 * math.sin(perp_angle),
                end_x - 3 * math.cos(perp_angle),
                end_y - 3 * math.sin(perp_angle),
                end_x + 3 * math.cos(perp_angle),
                end_y + 3 * math.sin(perp_angle)
            ]
            
            self.canvas.create_polygon(shaft_points, fill=color, outline='#000', width=1, tags=tag)
            
            # Lume dot at tip
            self.canvas.create_oval(
                end_x - 4, end_y - 4, end_x + 4, end_y + 4,
                fill='#90EE90', outline=color, width=1, tags=tag
            )
            
        elif hand_type == 'minute':
            # Minute hand with lume stripe
            perp_angle = angle_rad + math.pi/2
            shaft_width = width
            
            shaft_points = [
                self.center_x + shaft_width//2 * math.cos(perp_angle),
                self.center_y + shaft_width//2 * math.sin(perp_angle),
                self.center_x - shaft_width//2 * math.cos(perp_angle),
                self.center_y - shaft_width//2 * math.sin(perp_angle),
                end_x - 2 * math.cos(perp_angle),
                end_y - 2 * math.sin(perp_angle),
                end_x + 2 * math.cos(perp_angle),
                end_y + 2 * math.sin(perp_angle)
            ]
            
            self.canvas.create_polygon(shaft_points, fill=color, outline='#000', width=1, tags=tag)
            
            # Lume stripe
            lume_length = length * 0.7
            lume_end_x = self.center_x + lume_length * math.cos(angle_rad)
            lume_end_y = self.center_y + lume_length * math.sin(angle_rad)
            
            self.canvas.create_line(
                self.center_x, self.center_y, lume_end_x, lume_end_y,
                width=2, fill='#90EE90', tags=tag
            )
            
        else:  # Second hand
            # Red second hand with counterweight
            self.canvas.create_line(
                self.center_x, self.center_y, end_x, end_y,
                width=width, fill=color, capstyle=tk.ROUND, tags=tag
            )
            
            # Counterweight
            counter_length = 25
            counter_x = self.center_x - counter_length * math.cos(angle_rad)
            counter_y = self.center_y - counter_length * math.sin(angle_rad)
            
            self.canvas.create_line(
                self.center_x, self.center_y, counter_x, counter_y,
                width=width+1, fill=color, capstyle=tk.ROUND, tags=tag
            )
            
            # Second hand tip
            self.canvas.create_oval(
                end_x - 3, end_y - 3, end_x + 3, end_y + 3,
                fill=color, outline='', tags=tag
            )
    
    def update_watch(self):
        """Update the watch display"""
        # Clear previous hands
        self.canvas.delete("hands")
        
        # Get current time
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec
        
        # Calculate angles with smooth movement
        second_angle = seconds * 6 + (time.time() % 1) * 6
        minute_angle = minutes * 6 + seconds * 0.1
        hour_angle = hours * 30 + minutes * 0.5
        
        # Draw hands in proper order (longest to shortest)
        self.draw_luxury_hands(second_angle, 110, 2, '#DC143C', 'second', "hands")
        self.draw_luxury_hands(minute_angle, 95, 5, '#E8E8E8', 'minute', "hands")
        self.draw_luxury_hands(hour_angle, 65, 7, '#E8E8E8', 'hour', "hands")
        
        # Center hub
        self.canvas.create_oval(
            self.center_x - 6, self.center_y - 6,
            self.center_x + 6, self.center_y + 6,
            fill='#FFD700', outline='#DAA520', width=2, tags="hands"
        )
        
        # Update date in date window
        self.canvas.delete("date")
        current_date = datetime.now()
        date_text = str(current_date.day)
        date_x = self.center_x + 45
        self.canvas.create_text(
            date_x, self.center_y, text=date_text,
            font=('Arial', 16, 'bold'), fill='black', tags="date"
        )
        
        # Digital time display
        time_str = time.strftime("%H:%M:%S", current_time)
        date_str = time.strftime("%A, %B %d, %Y", current_time)
        
        self.canvas.delete("digital_time")
        
        # Digital display background
        self.canvas.create_rectangle(
            self.center_x - 140, 650, self.center_x + 140, 710,
            fill='#1a1a1a', outline='#DAA520', width=2, tags="digital_time"
        )
        
        self.canvas.create_text(
            self.center_x, 670, text=time_str,
            font=('Digital', 18, 'bold'), fill='#00FF00', tags="digital_time"
        )
        
        self.canvas.create_text(
            self.center_x, 690, text=date_str,
            font=('Arial', 11), fill='#90EE90', tags="digital_time"
        )
        
        # Rotate bezel slightly for animation effect
        self.bezel_rotation += 0.1
        if self.bezel_rotation >= 360:
            self.bezel_rotation = 0
        
        # Schedule next update
        self.root.after(50, self.update_watch)

def main():
    root = tk.Tk()
    watch = LuxuryWatchClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()