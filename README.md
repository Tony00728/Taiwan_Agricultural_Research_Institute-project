# Taiwan_Agricultural_Research_Institute-project-鳳梨釋迦果樹影像蒐集與偵測辨識


Reference papers - [YOLOv3: An Incremental Improvement](https://arxiv.org/abs/1804.02767)


鳳梨釋迦果樹影像-修枝前
<img src="./atemoya_img/train/00_GH011475_60.jpg" height="480">

鳳梨釋迦果樹影像-剪枝後
<img src="./atemoya_img/train/01_GH011499_26.jpg" height="480">


鳳梨釋迦果樹影像-開花授粉期
<img src="./atemoya_img/train/02_GH012540_134.jpg" height="480">

鳳梨釋迦果樹影像-結實期
<img src="./atemoya_img/train/03_GH012535_64.jpg" height="480">

鳳梨釋迦果樹影像-套袋期
<img src="./atemoya_img/train/04_GH011485_40.jpg" height="480">

## Label dataset
利用LabelImg影像標註工具



## Training
創個yaml檔案.data/kitti.yaml，裡面要有訓練集、驗證集、測試集路徑位址，以及打上所有類別例如:第0類修枝期為tree_00、第1類剪枝期為tree_01、第2類開花授粉期為tree_02、第3類結實期為tree_03、第4類套袋期為tree_04
```
python train.py
```

## Detect
```
python detect.py
```
## Testing

[review_object_detection_metrics](https://github.com/rafaelpadilla/review_object_detection_metrics)

## Citation

```
@article{redmon2018yolov3,
  title={Yolov3: An incremental improvement},
  author={Redmon, Joseph and Farhadi, Ali},
  journal={arXiv preprint arXiv:1804.02767},
  year={2018}
}
```
