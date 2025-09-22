import webview


class DreamAPI:
    @staticmethod
    def start(self,answers):
        Q1, Q2, Q3, Q4, Q5 = answers
        Q4_response = "Perfect" if Q4.strip().lower() == "yes" else "That's OK"
        
        prediction = (
        f"Your chosen career is to be {Q1}.\n"
        f"The best school to graduate from is {Q2}.\n"
        f"Your expected salary will be {Q3}.\n"
        f"{Q4_response} regarding a backup career.\n"
        f"Because you have chosen {Q5}.\n"
        "You have perfectly chosen your career and are set for life!"
)
        print("\n--- Dream Quiz Summary ---")
        
        
        
        return prediction
    
if __name__ == "__main__":
    api = DreamAPI()
    window = webview.create_window("Dream Quiz App", "index.html", js_api=api)
    webview.start()
        