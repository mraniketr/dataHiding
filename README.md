# dataHiding
A python application to hide any sort of data into an image.

## Encryption

### STEP 1:
Put an image named *final.jpg* in the current working directory.

### STEP 2:
Run the application:

```
python3 dataHIDING.py
```

### STEP 3:
Choose option 1 to encrypt data:

```
1. Create classified image 
2. Extract Data 

1
Encryption successful
```

*All the data inside the selected folder will be compressed into a zip file and merged with final.jpg.*
  
## Decryption

### STEP 1:
Run the application:

```
python3 dataHIDING.py
```
  
### STEP 2:
Choose option 2 to decrypt data:

```
1. Create classified image 
2. Extract Data 

2
Archive:  classified.jpg
warning [classified.jpg]:  1018280 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: payload.txt             
Extraction successful
```
*The jpg will be extracted into the current directory.*
