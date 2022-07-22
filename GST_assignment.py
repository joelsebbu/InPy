
def calculate():
    # input price and gst rate
    price = int(input("Enter the price: "))
    gst_rate = int(input("Enter the gst rate: "))
    # calculate gst
    gst = price * gst_rate / 100
    print("GST: ", gst)

    # calculate total price
    total_price = price + gst
    print("Total price: ", total_price)

    #calculate cgst and sgst
    cgst = gst / 2
    sgst = gst / 2
    print("CGST: ", cgst)
    print("SGST: ", sgst)

calculate()
