def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} Chai....")
        if flavor == "unknown":
            raise ValueError ("We don't know this flavor")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"{flavor} chai is ready")
    finally:
        print("Next Customer Please")


serve_chai("Masala")
serve_chai("unknown")