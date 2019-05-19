"""
生成配置文件 .json格式
直接运行即可
"""
import json
if __name__ == "__main__":
    paths = {
        'COCO_Path':'E:\\COCO',
        'Annotation_Path':'E:\\COCO\\annotations_trainval2017',
        'Annotation_Files':['captions_train2017.json', 'captions_val2017.json', 'instances_train2017.json','instances_val2017.json', 'person_keypoints_train2017.json', 'person_keypoints_val2017.json'],
        'Train_ZIP':"E:\\COCO\\train2017.zip",
        'Val_ZIP':"E:\\COCO\\val2017.zip"
    }
    with open("..\\data\\config.json", "w") as f:
        json.dump(paths, f)