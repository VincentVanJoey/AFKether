import wx
import time
import threading
import pyautogui
import AFKether_Setup
from AFKether_GUI import MainFrame 

base_prices = {
    "Icon": 2000,
    "Emote": 12000,
    "Pallet": 16000,
    "Skin": 50000,
    "Respawn Platform": 12000,
    "Death Effect": 12000,
    "Taunt": 7500,
}

rarity_multipliers = {
    "Icon": {"Common": 1, "Rare": 2, "Epic": 4},
    "Emote": {"Rare": 1, "Epic": 1.5},
    "Pallet": {"Common": 1, "Rare": 2, "Epic": 3},
    "Skin": {"Common": 1, "Rare": 2, "Epic": 3},
    "Respawn Platform": {"Common": 1, "Rare": 1.5, "Epic": 2},
    "Death Effect": {"Common": 1, "Rare": 1.5, "Epic": 2},
    "Taunt": {"Epic": 1},  # Even though taunts are (so far) only epic, this is included for consistency
}

class MainWindow(MainFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.frame_notebook.SetSelection(0)
        self.config_path = AFKether_Setup.get_config_path()
        self.theme_color = AFKether_Setup.read_from_config(self.config_path, "theme_color")
        if self.theme_color:
            self.set_theme(self.theme_color)
        else:
            self.set_theme((116,85,135,0))

        self.loop_running = False
        self.loop_event = threading.Event()

        import vgamepad as vg
        self.vg = vg
        self.gamepad = vg.VX360Gamepad()
    
        self.calcs = []
        self.last_calc = None
        self.total_price = 0

        self.target_window = None

    def on_close(self, event):
        return super().on_close(event)

    #region Loop methods
    def switch_to_window(self, title):
        try:
            print("Swapping")
            self.target_window = pyautogui.getWindowsWithTitle(title)[0]
            
            try:
                self.target_window.activate()
            except:
                self.target_window.minimize()
                self.target_window.maximize()
                self.target_window.activate()
            return True
        except IndexError:
            return False

    def on_toggle_press(self, event):
        
        if self.toggle_btn.GetValue():
            self.loop_event.set()  # Signal the thread to run
            self.toggle_btn.SetLabel("Stop Loop")
            self.loop_thread = threading.Thread(target=self.run_loop)
            self.loop_thread.daemon = True
            self.loop_thread.start()

            print("Loop started.")
        else: 
            self.loop_event.clear()
            self.toggle_btn.SetLabel("Start Loop")
            print("Loop stopped.")

    def run_loop(self):
        time_to_wait = self.minute_spin.GetValue() * 60
        self.switch_to_window("Rivals2")
        while self.loop_event.is_set():
            
            #Controller is awake
            self.wake_up()
            
            self.press_button(self.vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            self.press_button(self.vg.XUSB_BUTTON.XUSB_GAMEPAD_START)

            # Match Start
            for i in range(time_to_wait + 16):
                if not self.loop_event.is_set():
                    print("Loop interrupted during wait.")
                    return
                time.sleep(1)
            
            # Results Screen
            if not self.loop_event.is_set():
                print("Loop interrupted before results screen.")
                return
            
            if self.switch_to_window("Rivals2"):
                time.sleep(3.0)
                self.press_button(self.vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
                self.press_button(self.vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            
        print("Loop thread exiting.")
    #endregion

    #region Calc methods

    def calc_print_total(self):
        self.total_amount.SetValue(f"Total Coins: {self.total_price:,}\n" \
                            f"Total Bucks: { int(self.total_price / 100) }\n" \
                            f"USD: {self.total_price / 10000 :.2f}\n"
                            f"---------------------------"
                            f"{'\n'.join(self.calcs)}"
                            )

    def calc_add_item(self, event):
        item_type = self.item_type_choice.GetStringSelection()
        item_rarity = self.rarity_type_choice.GetStringSelection()
        item_count = self.item_count_spin.GetValue()

        if not item_type or not item_rarity:
            return
        
        # Base price and rarity multiplier lookup
        item_price = base_prices.get(item_type)
        if item_price is None:
            wx.MessageBox(f"Item type '{item_type}' is not supported.", "Error")
            return

        price_mult = rarity_multipliers.get(item_type, {}).get(item_rarity)
        if price_mult is None:
            wx.MessageBox(f"Rarity '{item_rarity}' not valid for type '{item_type}'.", "Error")
            return

        self.total_price += item_price * price_mult * item_count
        
        new_calc = f"{item_rarity} {item_type} x{item_count}"
        self.calcs.append(new_calc)
        self.last_calc = new_calc

        self.calc_print_total()


    def calc_undo_item(self, event):
        if not self.calcs:
            return
        self.calcs.pop()
        last_part_parts = self.last_calc.split(" ")
        self.total_price -= base_prices.get(last_part_parts[1]) * rarity_multipliers.get(last_part_parts[1], {}).get(last_part_parts[0]) * last_part_parts[2][2]
        self.calc_print_total()
        self.last_calc = self.calcs[-1]


    def calc_clear_item(self, event):
        if not self.calcs:
            return
        self.calcs.clear()
        self.total_price = 0
        self.calc_print_total()
        self.last_calc = None
    
    #endregion

    #region Help methods

    def set_theme(self, color):
        self.main_panel.SetBackgroundColour(color)
        self.calc_panel.SetBackgroundColour(color)
        self.open_config_btn.SetBackgroundColour(color)

    def help_open_config(self, event):
        AFKether_Setup.open_config(self.config_path)
    
    def help_theme_color_change(self, event):
        new_color = event.GetColour().Get(True) #gets the color in serializable form?
        self.set_theme(new_color)
        AFKether_Setup.write_to_config(self.config_path, "theme_color", new_color)
    
    #endregion

    #region virtual controller methods
    def wake_up(self):
        # press a button to wake the device up
        time.sleep(2.0)
        self.gamepad.press_button(button=self.vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        self.gamepad.update()
        time.sleep(0.5)
        self.gamepad.release_button(button=self.vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        self.gamepad.update()
        time.sleep(0.5)

    def press_button(self, to_press):
        # press buttons and things
        self.gamepad.press_button(button=to_press)
        self.gamepad.update()
        time.sleep(0.5)
        self.gamepad.release_button(button=to_press)
        self.gamepad.update()
        time.sleep(0.5)

    def reset_to_default(self):
        # reset gamepad to default state
       self.gamepad.reset()
       self.gamepad.update()
    #endregion

if __name__=="__main__":
    app = wx.App(False)
    AFKether_Setup.check_vigem_installed()
    frame = MainWindow(None)
    frame.Show()
    app.MainLoop()