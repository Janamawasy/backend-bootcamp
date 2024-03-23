import sensor_simulator
from massanger import Massanger
from analyzer import Analyzer

def main():
    msg = Massanger()
    sensor_simulator.generate_records(5, msg)
    analyzer = Analyzer(100, msg)
    analyzer.manage_analyzer()

main()

