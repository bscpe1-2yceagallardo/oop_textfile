from even_and_odd_separation import NumberDistinguisher

processor = NumberDistinguisher("numbers.txt")
processor.scan_and_distinguish()
processor.saving_results()
processor.computing_statistics()
processor.showing_summary()