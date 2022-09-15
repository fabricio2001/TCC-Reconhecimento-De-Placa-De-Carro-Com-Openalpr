from openalpr import Alpr

alpr = Alpr("br", "openalpr.conf","runtime_data")

if not alpr.is_loaded():
    print("Error loading openalpr")
    sys.exit(1)

alpr.set_top_n(20)
alpr.set_default_region("br")

result = alpr.recognize_file("resource/img/carro1.jpg")

print(result)