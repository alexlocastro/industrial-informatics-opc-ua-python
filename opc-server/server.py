from opcua import Server, ua
from gpiozero import Button, LED
import time

#Creates an instance of our OPC UA server
server = Server()

#Sets the endpoint url
url = "opc.tcp://10.42.0.2:4840/OPCUAproject"
server.set_endpoint(url)

#Sets the available security policies and loads server certificate and private key
server.set_security_policy([ua.SecurityPolicyType.NoSecurity,
                            ua.SecurityPolicyType.Basic256Sha256_Sign,
                            ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt])

server.load_certificate("certificate.pem")
server.load_private_key("key.pem")

#Creates a new namespace
name = "OPCUA_PROJECT_SERVER"
addspace = server.register_namespace(name)

#Gets the Objects node
node = server.get_objects_node()

#Adds a dev Object in our newly created namespace
dev = node.add_object(addspace, "Devices")

#Adds the variables to control the led and send our button status
buttonVariable = dev.add_variable(addspace, "Button", ua.Variant(0, ua.VariantType.Boolean))
ledVariable = dev.add_variable(addspace, "Led", ua.Variant(0, ua.VariantType.Boolean))

buttonVariable.set_writable()
ledVariable.set_writable()

#Starts the server and prints the url it's running at
server.start()

print(f"Server started at {url}")

#Variables to handle the GPIO pins
button = Button(21)
led = LED(17)

try:
    #Loop that updates the button varible status and toggles the led
    #based on the OPC ledVariable 
    while True:
        buttonVariable.set_value(1 if button.is_pressed else 0)
        ledValue = ledVariable.get_value()
        if ledValue:
            led.on()
        else:
            led.off()
        time.sleep(0.1)
except:
    print("Shutting down the server...")
finally:
    server.stop()


