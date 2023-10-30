import base64
import zlib
import io

def compress_image(image_data, quality=10):
    try:
        # Decode the base64 image string
        image_bytes = base64.b64decode(image_data)

        # Compress the image using zlib
        compressed_image = zlib.compress(image_bytes, quality)

        # Encode the compressed image as base64
        compressed_base64 = base64.b64encode(compressed_image).decode("utf-8")

        return compressed_base64
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Example base64 image string
    base64_image = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAAFElEQVR42mP8z/CfAwAA/ADQMwBIr1wAAAAASUVORK5CYII="

    # Compress the image and get the result as a base64 string
    compressed_image = compress_image(base64_image, quality=10)

    # Print the compressed image (as a base64 string)
    print(compressed_image)
