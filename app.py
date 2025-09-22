import webview


class DreamAPI:
    def start(self):
        print("Lets Begin Your Dream Quiz!!!")
        
        
        Q1 = input("What do you want to be when you grow up?")
        
        Q2 = input("Which school do you want to go to for your dream?")
        
        Q3 = input("How much will you earn from your chosen carrer?")
        
        while True:
            Q4 = input("Q4: Do you have a backup career? (yes/no) ")
            if Q4.strip().lower() == "yes":
                print("Perfect")
                break
            elif Q4.strip().lower() == "no":
                print("That's OK")
                break
            else:
                print("Please answer 'yes' or 'no'.")
            
        
        Q5 = bool("Do You truly believe in your chose carrer?")
        
        prediction = (
        f"Your chosen career is to be {Q1}.\n"
        f"The best school to graduate from is {Q2}.\n"
        f"Your expected salary will be {Q3}.\n"
        f"Because you have chosen {Q5}.\n"
        "You have perfectly chosen your career and are set for life!"
)
        print("\n--- Dream Quiz Summary ---")
        
        
        
        return prediction
    
if __name__ == "__main__":
    api = DreamAPI()
    window = webview.create_window("Dream Quiz App", "index.html", js_api=api)
    webview.start()
        