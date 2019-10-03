from random import randint

class Strategy:
    def __init__(self, locator_type, detector_type, labels):
        if locator_type == 'caffe':
            self.text_locator = CaffeLocator(labels)
        else:
            self.text_locator = OpencvLocator(labels)
        if detector_type == 'caffe':
            self.text_detector = CaffeDetector(labels)
        else:
            self.text_detector = OpencvDetector(labels)

    def process_image(self, image):
        print('Not processed image:     ' + image)
        image = self.text_locator.locate_text(image)
        print('Text located on image:   ' + image)
        image = self.text_detector.detect_text(image)
        print('Text detected on image:  ' + image)

class CaffeLocator:
    def __init__(self, labels):
        self.labels = labels

    def locate_text(self, image):
        str_img = str(image)
        return 'text_located_by_caffe_'+str_img+'label'+str(self.labels[0])


class OpencvLocator:
    def __init__(self, labels):
        self.labels = labels

    def locate_text(self, image):
        str_img = str(image)
        return 'text_located_by_opencv_'+str_img+'label'+str(self.labels[-1])


class CaffeDetector:
    def __init__(self, labels):
        self.labels = labels

    def detect_text(self, image):
        return str(image)+str(self.labels[randint(0, len(self.labels))])+'_detected_by_Caffe'


class OpencvDetector:
    def __init__(self, labels):
        self.labels = labels

    def detect_text(self, image):
        return str(image)+str(self.labels)+'_detected_by_opencv'

if __name__ == '__main__':
    labels = [1,2,3,4,57,9,3,463]
    image = 'MyIMAGE'
    strategy_a = Strategy('caffe', 'caffe', labels)
    strategy_b = Strategy('opencv', 'opencv', labels)
    strategy_c = Strategy('caffe', 'opencv', labels)
    strategy_d = Strategy('opencv', 'caffe', labels)
    strategy_a.process_image(image)
    strategy_b.process_image(image)
    strategy_c.process_image(image)
    strategy_d.process_image(image)