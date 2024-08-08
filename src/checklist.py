class Checklist:
    def __init__(self):
        self.questions = [
            "We have or expect to have many data-sharing partners",
            "Our partners change frequently",
            "We deal with large volumes of data",
            "Our data is highly diverse (many types/formats)",
            "Real-time or near-real-time data sharing is crucial",
            "We need fine-grained access control",
            "Data sovereignty is a major concern",
            "We must comply with strict data protection regulations",
            "We need to integrate data from multiple, heterogeneous sources",
            "Standardized data exchange formats are crucial for our operations",
            "We anticipate significant growth in data volume or partners",
            "We need a solution that can easily accommodate new use cases",
            "We require a platform for collaborative data analysis",
            "Data marketplaces are relevant to our business model",
            "We want to leverage advanced technologies (AI, ML, blockchain)",
            "We need a unified platform for data management and sharing"
        ]
        self.responses = []

    def run_checklist(self):
        print("Please rate each statement from 1 (Strongly Disagree) to 5 (Strongly Agree):")
        for question in self.questions:
            while True:
                try:
                    response = int(input(f"{question}: "))
                    if 1 <= response <= 5:
                        self.responses.append(response)
                        break
                    else:
                        print("Please enter a number between 1 and 5.")
                except ValueError:
                    print("Please enter a valid number.")

    def calculate_score(self):
        return sum(self.responses)

    def interpret_score(self):
        score = self.calculate_score()
        if score <= 35:
            return "Traditional data sharing methods may suffice"
        elif score <= 55:
            return "Consider implementing a data space"
        else:
            return "Strongly consider implementing a data space"

if __name__ == "__main__":
    checklist = Checklist()
    checklist.run_checklist()
    print(f"Your score: {checklist.calculate_score()}")
    print(f"Interpretation: {checklist.interpret_score()}")
