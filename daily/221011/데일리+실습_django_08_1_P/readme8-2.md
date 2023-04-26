models.py
200 200 으로 맞추기 위해 썸네일 추가
```py
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField


    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200,200)],
        format='JPEG',
        options={'quality': 80},
    )
```

detail.html
썸네일로 변경
```html
    <img src="{{ memo.image_thumbnail.url }}" alt="{{ memo.image_thumbnail }}">
```


![image](./detail_2.png)
![image](./update_2.png)