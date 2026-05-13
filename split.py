import os
import random
import shutil


base_dir = 'datasets'
train_images = os.path.join(base_dir, 'train', 'images')
train_labels = os.path.join(base_dir, 'train', 'labels')

def split_data():
    if not os.path.exists(train_images):
        print(f"Error: Folder {train_images} not found. First, put the dataset in datasets/train.")
        return


    for split in ['valid', 'test']:
        for sub in ['images', 'labels']:
            os.makedirs(os.path.join(base_dir, split, sub), exist_ok=True)


    images = [f for f in os.listdir(train_images) if f.endswith(('.jpg', '.png', '.jpeg'))]
    random.shuffle(images)

    total = len(images)
    val_count = int(total * 0.2)
    test_count = int(total * 0.1)

    val_files = images[:val_count]
    test_files = images[val_count : val_count + test_count]

    def move_files(files, target_split):
        for name in files:

            shutil.move(os.path.join(train_images, name), 
                        os.path.join(base_dir, target_split, 'images', name))
            

            label_name = os.path.splitext(name)[0] + '.txt'
            label_src = os.path.join(train_labels, label_name)
            if os.path.exists(label_src):
                shutil.move(label_src, 
                            os.path.join(base_dir, target_split, 'labels', label_name))

    move_files(val_files, 'valid')
    move_files(test_files, 'test')

if __name__ == '__main__':
    split_data()