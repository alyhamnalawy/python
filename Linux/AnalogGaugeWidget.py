import os
@@ -27,7 +27,7 @@

    from PyQt5.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont, QPainter, QFontMetrics, QConicalGradient, QRadialGradient, QFontDatabase

    from PyQt5.QtCore import Qt ,QTime, QTimer, QPoint, QPointF, QRect, QSize, QObject, pyqtSignal
    from PyQt5.QtCore import Qt, QTime, QTimer, QPoint, QPointF, QRect, QSize, QObject, pyqtSignal

except:
    print("Error while importing PyQt5")
@@ -36,11 +36,13 @@
################################################################################################
# AnalogGaugeWidget CLASS
################################################################################################


class AnalogGaugeWidget(QWidget):
    """Fetches rows from a Bigtable.
    Args: 
        none
    
    """
    valueChanged = pyqtSignal(int)

@@ -136,8 +138,9 @@ def __init__(self, parent=None):

        ################################################################################################
        # LOAD CUSTOM FONT
        ################################################################################################     
        QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), 'fonts/Orbitron/Orbitron-VariableFont_wght.ttf') )
        ################################################################################################
        QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(
            __file__), 'fonts/Orbitron/Orbitron-VariableFont_wght.ttf'))

        ################################################################################################
        # DEFAULT POLYGON COLOR
@@ -248,95 +251,95 @@ def setValueFontFamily(self, font):
    # SET BIG SCALE COLOR
    ################################################################################################
    def setBigScaleColor(self, color):
        self.bigScaleMarker = QColor(color)      
        self.bigScaleMarker = QColor(color)

    ################################################################################################
    # SET FINE SCALE COLOR
    ################################################################################################
    def setFineScaleColor(self, color):
        self.fineScaleColor = QColor(color)    
        self.fineScaleColor = QColor(color)

    ################################################################################################
    # GAUGE THEMES
    ################################################################################################
    def setGaugeTheme(self, Theme = 1):
    def setGaugeTheme(self, Theme=1):
        if Theme == 0 or Theme == None:
            self.set_scale_polygon_colors([[.00, Qt.red],
                                    [.1, Qt.yellow],
                                    [.15, Qt.green],
                                    [1, Qt.transparent]])
                                           [.1, Qt.yellow],
                                           [.15, Qt.green],
                                           [1, Qt.transparent]])

            self.needle_center_bg = [
                                    [0, QColor(35, 40, 3, 255)], 
                                    [0.16, QColor(30, 36, 45, 255)], 
                                    [0.225, QColor(36, 42, 54, 255)], 
                                    [0.423963, QColor(19, 23, 29, 255)], 
                                    [0.580645, QColor(45, 53, 68, 255)], 
                                    [0.792627, QColor(59, 70, 88, 255)], 
                                    [0.935, QColor(30, 35, 45, 255)], 
                                    [0, QColor(35, 40, 3, 255)],
                                    [0.16, QColor(30, 36, 45, 255)],
                                    [0.225, QColor(36, 42, 54, 255)],
                                    [0.423963, QColor(19, 23, 29, 255)],
                                    [0.580645, QColor(45, 53, 68, 255)],
                                    [0.792627, QColor(59, 70, 88, 255)],
                                    [0.935, QColor(30, 35, 45, 255)],
                                    [1, QColor(35, 40, 3, 255)]
                                    ]
            ]

            self.outer_circle_bg =  [
                                    [0.0645161, QColor(30, 35, 45, 255)], 
                                    [0.37788, QColor(57, 67, 86, 255)], 
                                    [1, QColor(30, 36, 45, 255)]
                                    ]
            self.outer_circle_bg = [
                [0.0645161, QColor(30, 35, 45, 255)],
                [0.37788, QColor(57, 67, 86, 255)],
                [1, QColor(30, 36, 45, 255)]
            ]

        if Theme == 1:
            self.set_scale_polygon_colors([[.75, Qt.red],
                                     [.5, Qt.yellow],
                                     [.25, Qt.green]])
                                           [.5, Qt.yellow],
                                           [.25, Qt.green]])

            self.needle_center_bg = [
                                    [0, QColor(35, 40, 3, 255)], 
                                    [0.16, QColor(30, 36, 45, 255)], 
                                    [0.225, QColor(36, 42, 54, 255)], 
                                    [0.423963, QColor(19, 23, 29, 255)], 
                                    [0.580645, QColor(45, 53, 68, 255)], 
                                    [0.792627, QColor(59, 70, 88, 255)], 
                                    [0.935, QColor(30, 35, 45, 255)], 
                                    [0, QColor(35, 40, 3, 255)],
                                    [0.16, QColor(30, 36, 45, 255)],
                                    [0.225, QColor(36, 42, 54, 255)],
                                    [0.423963, QColor(19, 23, 29, 255)],
                                    [0.580645, QColor(45, 53, 68, 255)],
                                    [0.792627, QColor(59, 70, 88, 255)],
                                    [0.935, QColor(30, 35, 45, 255)],
                                    [1, QColor(35, 40, 3, 255)]
                                    ]
            ]

            self.outer_circle_bg =  [
                                    [0.0645161, QColor(30, 35, 45, 255)], 
                                    [0.37788, QColor(57, 67, 86, 255)], 
                                    [1, QColor(30, 36, 45, 255)]
                                    ]
            self.outer_circle_bg = [
                [0.0645161, QColor(30, 35, 45, 255)],
                [0.37788, QColor(57, 67, 86, 255)],
                [1, QColor(30, 36, 45, 255)]
            ]

        if Theme == 2:
            self.set_scale_polygon_colors([[.25, Qt.red],
                                     [.5, Qt.yellow],
                                     [.75, Qt.green]])
                                           [.5, Qt.yellow],
                                           [.75, Qt.green]])

            self.needle_center_bg = [
                                    [0, QColor(35, 40, 3, 255)], 
                                    [0.16, QColor(30, 36, 45, 255)], 
                                    [0.225, QColor(36, 42, 54, 255)], 
                                    [0.423963, QColor(19, 23, 29, 255)], 
                                    [0.580645, QColor(45, 53, 68, 255)], 
                                    [0.792627, QColor(59, 70, 88, 255)], 
                                    [0.935, QColor(30, 35, 45, 255)], 
                                    [0, QColor(35, 40, 3, 255)],
                                    [0.16, QColor(30, 36, 45, 255)],
                                    [0.225, QColor(36, 42, 54, 255)],
                                    [0.423963, QColor(19, 23, 29, 255)],
                                    [0.580645, QColor(45, 53, 68, 255)],
                                    [0.792627, QColor(59, 70, 88, 255)],
                                    [0.935, QColor(30, 35, 45, 255)],
                                    [1, QColor(35, 40, 3, 255)]
                                    ]
            ]

            self.outer_circle_bg =  [
                                    [0.0645161, QColor(30, 35, 45, 255)], 
                                    [0.37788, QColor(57, 67, 86, 255)], 
                                    [1, QColor(30, 36, 45, 255)]
                                    ]
            self.outer_circle_bg = [
                [0.0645161, QColor(30, 35, 45, 255)],
                [0.37788, QColor(57, 67, 86, 255)],
                [1, QColor(30, 36, 45, 255)]
            ]

        elif Theme == 3:
            self.set_scale_polygon_colors([[.00, Qt.white]])

            self.needle_center_bg = [
                                    [0, Qt.white], 
                                    ]
                                    [0, Qt.white],
            ]

            self.outer_circle_bg =  [
                                    [0, Qt.white], 
                                    ]
            self.outer_circle_bg = [
                [0, Qt.white],
            ]

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black
@@ -345,235 +348,234 @@ def setGaugeTheme(self, Theme = 1):
            self.set_scale_polygon_colors([[1, Qt.black]])

            self.needle_center_bg = [
                                    [0, Qt.black], 
                                    ]
                                    [0, Qt.black],
            ]

            self.outer_circle_bg =  [
                                    [0, Qt.black], 
                                    ]
            self.outer_circle_bg = [
                [0, Qt.black],
            ]

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 5:
            self.set_scale_polygon_colors([[1, QColor("#029CDE")]])  
            self.set_scale_polygon_colors([[1, QColor("#029CDE")]])

            self.needle_center_bg = [
                                    [0, QColor("#029CDE")], 
                                    ]
                                    [0, QColor("#029CDE")],
            ]

            self.outer_circle_bg =  [
                                    [0, QColor("#029CDE")], 
                                    ]
            self.outer_circle_bg = [
                [0, QColor("#029CDE")],
            ]

        elif Theme == 6:
            self.set_scale_polygon_colors([[.75, QColor("#01ADEF")],
                                     [.5, QColor("#0086BF")],
                                     [.25, QColor("#005275")]])
                                           [.5, QColor("#0086BF")],
                                           [.25, QColor("#005275")]])

            self.needle_center_bg = [
                                    [0, QColor(0, 46, 61, 255)], 
                                    [0.322581, QColor(1, 173, 239, 255)], 
                                    [0, QColor(0, 46, 61, 255)],
                                    [0.322581, QColor(1, 173, 239, 255)],
                                    [0.571429, QColor(0, 73, 99, 255)],
                                    [1, QColor(0, 46, 61, 255)]
                                    ]
            ]

            self.outer_circle_bg =  [
                                    [0.0645161, QColor(0, 85, 116, 255)], 
                                    [0.37788, QColor(1, 173, 239, 255)], 
                                    [1, QColor(0, 69, 94, 255)]
                                    ]
            self.outer_circle_bg = [
                [0.0645161, QColor(0, 85, 116, 255)],
                [0.37788, QColor(1, 173, 239, 255)],
                [1, QColor(0, 69, 94, 255)]
            ]

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 7:
            self.set_scale_polygon_colors([[.25, QColor("#01ADEF")],
                                     [.5, QColor("#0086BF")],
                                     [.75, QColor("#005275")]])
                                           [.5, QColor("#0086BF")],
                                           [.75, QColor("#005275")]])

            self.needle_center_bg = [
                                    [0, QColor(0, 46, 61, 255)], 
                                    [0.322581, QColor(1, 173, 239, 255)], 
                                    [0, QColor(0, 46, 61, 255)],
                                    [0.322581, QColor(1, 173, 239, 255)],
                                    [0.571429, QColor(0, 73, 99, 255)],
                                    [1, QColor(0, 46, 61, 255)]
                                    ]
            ]

            self.outer_circle_bg =  [
                                    [0.0645161, QColor(0, 85, 116, 255)], 
                                    [0.37788, QColor(1, 173, 239, 255)], 
                                    [1, QColor(0, 69, 94, 255)]
                                    ]
            self.outer_circle_bg = [
                [0.0645161, QColor(0, 85, 116, 255)],
                [0.37788, QColor(1, 173, 239, 255)],
                [1, QColor(0, 69, 94, 255)]
            ]

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 8:
            self.setCustomGaugeTheme(
                color1 = "#ffaa00",
                color2= "#7d5300",
                color3 = "#3e2900"
                color1="#ffaa00",
                color2="#7d5300",
                color3="#3e2900"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 9:
            self.setCustomGaugeTheme(
                color1 = "#3e2900",
                color2= "#7d5300",
                color3 = "#ffaa00"
                color1="#3e2900",
                color2="#7d5300",
                color3="#ffaa00"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 10:
            self.setCustomGaugeTheme(
                color1 = "#ff007f",
                color2= "#aa0055",
                color3 = "#830042"
                color1="#ff007f",
                color2="#aa0055",
                color3="#830042"
            )


            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 11:
            self.setCustomGaugeTheme(
                color1 = "#830042",
                color2= "#aa0055",
                color3 = "#ff007f"
                color1="#830042",
                color2="#aa0055",
                color3="#ff007f"
            )
            

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 12:
            self.setCustomGaugeTheme(
                color1 = "#ffe75d",
                color2= "#896c1a",
                color3 = "#232803"
                color1="#ffe75d",
                color2="#896c1a",
                color3="#232803"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 13:
            self.setCustomGaugeTheme(
                color1 = "#ffe75d",
                color2= "#896c1a",
                color3 = "#232803"
                color1="#ffe75d",
                color2="#896c1a",
                color3="#232803"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 14:
            self.setCustomGaugeTheme(
                color1 = "#232803",
                color2= "#821600",
                color3 = "#ffe75d"
                color1="#232803",
                color2="#821600",
                color3="#ffe75d"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 15:
            self.setCustomGaugeTheme(
                color1 = "#00FF11",
                color2= "#00990A",
                color3 = "#002603"
                color1="#00FF11",
                color2="#00990A",
                color3="#002603"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 16:
            self.setCustomGaugeTheme(
                color1 = "#002603",
                color2= "#00990A",
                color3 = "#00FF11"
                color1="#002603",
                color2="#00990A",
                color3="#00FF11"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 17:
            self.setCustomGaugeTheme(
                color1 = "#00FFCC",
                color2= "#00876C",
                color3 = "#00211B"
                color1="#00FFCC",
                color2="#00876C",
                color3="#00211B"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 18:
            self.setCustomGaugeTheme(
                color1 = "#00211B",
                color2= "#00876C",
                color3 = "#00FFCC"
                color1="#00211B",
                color2="#00876C",
                color3="#00FFCC"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 19:
            self.setCustomGaugeTheme(
                color1 = "#001EFF",
                color2= "#001299",
                color3 = "#000426"
                color1="#001EFF",
                color2="#001299",
                color3="#000426"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 20:
            self.setCustomGaugeTheme(
                color1 = "#000426",
                color2= "#001299",
                color3 = "#001EFF"
                color1="#000426",
                color2="#001299",
                color3="#001EFF"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 21:
            self.setCustomGaugeTheme(
                color1 = "#F200FF",
                color2= "#85008C",
                color3 = "#240026"
                color1="#F200FF",
                color2="#85008C",
                color3="#240026"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 22:
            self.setCustomGaugeTheme(
                color1 = "#240026",
                color2= "#85008C",
                color3 = "#F200FF"
                color1="#240026",
                color2="#85008C",
                color3="#F200FF"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 23:
            self.setCustomGaugeTheme(
                color1 = "#FF0022",
                color2= "#080001",
                color3 = "#009991"
                color1="#FF0022",
                color2="#080001",
                color3="#009991"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 24:
            self.setCustomGaugeTheme(
                color1 = "#009991",
                color2= "#080001",
                color3 = "#FF0022"
                color1="#009991",
                color2="#080001",
                color3="#FF0022"
            )

            self.bigScaleMarker = Qt.white
@@ -588,48 +590,53 @@ def setCustomGaugeTheme(self, **colors):
                if "color3" in colors and len(str(colors['color3'])) > 0:

                    self.set_scale_polygon_colors([[.25, QColor(str(colors['color1']))],
                                            [.5, QColor(str(colors['color2']))],
                                            [.75, QColor(str(colors['color3']))]])
                                                   [.5, QColor(
                                                       str(colors['color2']))],
                                                   [.75, QColor(str(colors['color3']))]])

                    self.needle_center_bg = [
                                            [0, QColor(str(colors['color3']))], 
                                            [0.322581, QColor(str(colors['color1']))], 
                                            [0.571429, QColor(str(colors['color2']))],
                                            [0, QColor(str(colors['color3']))],
                                            [0.322581, QColor(
                                                str(colors['color1']))],
                                            [0.571429, QColor(
                                                str(colors['color2']))],
                                            [1, QColor(str(colors['color3']))]
                                            ]
                    ]

                    self.outer_circle_bg =  [
                                            [0.0645161, QColor(str(colors['color3']))], 
                                            [0.36, QColor(str(colors['color1']))], 
                                            [1, QColor(str(colors['color2']))]
                                            ]
                    self.outer_circle_bg = [
                        [0.0645161, QColor(str(colors['color3']))],
                        [0.36, QColor(
                            str(colors['color1']))],
                        [1, QColor(str(colors['color2']))]
                    ]

                else:

                    self.set_scale_polygon_colors([[.5, QColor(str(colors['color1']))],
                                             [1, QColor(str(colors['color2']))]])
                                                   [1, QColor(str(colors['color2']))]])

                    self.needle_center_bg = [
                                            [0, QColor(str(colors['color2']))], 
                                            [0, QColor(str(colors['color2']))],
                                            [1, QColor(str(colors['color1']))]
                                            ]
                    ]

                    self.outer_circle_bg =  [
                                            [0, QColor(str(colors['color2']))], 
                                            [1, QColor(str(colors['color2']))]
                                            ]
                    self.outer_circle_bg = [
                        [0, QColor(str(colors['color2']))],
                        [1, QColor(str(colors['color2']))]
                    ]

            else:

                self.set_scale_polygon_colors([[1, QColor(str(colors['color1']))]])
                self.set_scale_polygon_colors(
                    [[1, QColor(str(colors['color1']))]])

                self.needle_center_bg = [
                                        [1, QColor(str(colors['color1']))]
                                        ]
                ]

                self.outer_circle_bg =  [
                                        [1, QColor(str(colors['color1']))]
                                        ]
                self.outer_circle_bg = [
                    [1, QColor(str(colors['color1']))]
                ]

        else:

@@ -645,17 +652,19 @@ def setScalePolygonColor(self, **colors):
                if "color3" in colors and len(str(colors['color3'])) > 0:

                    self.set_scale_polygon_colors([[.25, QColor(str(colors['color1']))],
                                            [.5, QColor(str(colors['color2']))],
                                            [.75, QColor(str(colors['color3']))]])
                                                   [.5, QColor(
                                                       str(colors['color2']))],
                                                   [.75, QColor(str(colors['color3']))]])

                else:

                    self.set_scale_polygon_colors([[.5, QColor(str(colors['color1']))],
                                             [1, QColor(str(colors['color2']))]])
                                                   [1, QColor(str(colors['color2']))]])

            else:

                self.set_scale_polygon_colors([[1, QColor(str(colors['color1']))]])
                self.set_scale_polygon_colors(
                    [[1, QColor(str(colors['color1']))]])

        else:
            print("color1 is not defined")
@@ -669,24 +678,26 @@ def setNeedleCenterColor(self, **colors):
                if "color3" in colors and len(str(colors['color3'])) > 0:

                    self.needle_center_bg = [
                                            [0, QColor(str(colors['color3']))], 
                                            [0.322581, QColor(str(colors['color1']))], 
                                            [0.571429, QColor(str(colors['color2']))],
                                            [0, QColor(str(colors['color3']))],
                                            [0.322581, QColor(
                                                str(colors['color1']))],
                                            [0.571429, QColor(
                                                str(colors['color2']))],
                                            [1, QColor(str(colors['color3']))]
                                            ]
                    ]

                else:

                    self.needle_center_bg = [
                                            [0, QColor(str(colors['color2']))], 
                                            [0, QColor(str(colors['color2']))],
                                            [1, QColor(str(colors['color1']))]
                                            ]
                    ]

            else:

                self.needle_center_bg = [
                                        [1, QColor(str(colors['color1']))]
                                        ]
                ]
        else:
            print("color1 is not defined")

@@ -698,33 +709,33 @@ def setOuterCircleColor(self, **colors):
            if "color2" in colors and len(str(colors['color2'])) > 0:
                if "color3" in colors and len(str(colors['color3'])) > 0:

                    self.outer_circle_bg =  [
                                            [0.0645161, QColor(str(colors['color3']))], 
                                            [0.37788, QColor(str(colors['color1']))], 
                                            [1, QColor(str(colors['color2']))]
                                            ]
                    self.outer_circle_bg = [
                        [0.0645161, QColor(str(colors['color3']))],
                        [0.37788, QColor(
                            str(colors['color1']))],
                        [1, QColor(str(colors['color2']))]
                    ]

                else:

                    self.outer_circle_bg =  [
                                            [0, QColor(str(colors['color2']))], 
                                            [1, QColor(str(colors['color2']))]
                                            ]
                    self.outer_circle_bg = [
                        [0, QColor(str(colors['color2']))],
                        [1, QColor(str(colors['color2']))]
                    ]

            else:

                self.outer_circle_bg =  [
                                        [1, QColor(str(colors['color1']))]
                                        ]
                self.outer_circle_bg = [
                    [1, QColor(str(colors['color1']))]
                ]

        else:
            print("color1 is not defined")



    ################################################################################################
    # RESCALE
    ################################################################################################

    def rescale_method(self):
        # print("slotMethod")
        ################################################################################################
@@ -741,18 +752,19 @@ def rescale_method(self):
        self.change_value_needle_style([QPolygon([
            QPoint(4, 30),
            QPoint(-4, 30),
            QPoint(-2, - self.widget_diameter / 2 * self.needle_scale_factor),
            QPoint(0, - self.widget_diameter / 2 * self.needle_scale_factor - 6),
            QPoint(2, - self.widget_diameter / 2 * self.needle_scale_factor)
            QPoint(-2, int(- self.widget_diameter / 2 * self.needle_scale_factor)),
            QPoint(0, int(- self.widget_diameter /
                   2 * self.needle_scale_factor - 6)),
            QPoint(2, int(- self.widget_diameter / 2 * self.needle_scale_factor))
        ])])


        ################################################################################################
        # SET FONT SIZE
        ################################################################################################
        self.scale_fontsize = self.initial_scale_fontsize * self.widget_diameter / 400
        self.value_fontsize = self.initial_value_fontsize * self.widget_diameter / 400

        self.scale_fontsize = int(
            self.initial_scale_fontsize * self.widget_diameter / 400)
        self.value_fontsize = int(
            self.initial_value_fontsize * self.widget_diameter / 400)

    def change_value_needle_style(self, design):
        # prepared for multiple needle instrument
@@ -765,7 +777,7 @@ def change_value_needle_style(self, design):
    ################################################################################################
    # UPDATE VALUE
    ################################################################################################
    def updateValue(self, value, mouse_controlled = False):
    def updateValue(self, value, mouse_controlled=False):
        # if not mouse_controlled:
        #     self.value = value
        #
@@ -815,6 +827,7 @@ def setNeedleColor(self, R=50, G=50, B=50, Transparency=255):
    ################################################################################################
    # SET NEEDLE COLOR ON DRAG
    ################################################################################################

    def setNeedleColorOnDrag(self, R=50, G=50, B=50, Transparency=255):
        # Red: R = 0 - 255
        # Green: G = 0 - 255
@@ -863,7 +876,7 @@ def set_CenterPointColor(self, R=50, G=50, B=50, Transparency=255):
    ################################################################################################
    # SHOW HIDE NEEDLE POLYGON
    ################################################################################################
    def setEnableNeedlePolygon(self, enable = True):
    def setEnableNeedlePolygon(self, enable=True):
        self.enable_Needle_Polygon = enable

        if not self.use_timer_event:
@@ -872,7 +885,7 @@ def setEnableNeedlePolygon(self, enable = True):
    ################################################################################################
    # SHOW HIDE SCALE TEXT
    ################################################################################################
    def setEnableScaleText(self, enable = True):
    def setEnableScaleText(self, enable=True):
        self.enable_scale_text = enable

        if not self.use_timer_event:
@@ -881,7 +894,7 @@ def setEnableScaleText(self, enable = True):
    ################################################################################################
    # SHOW HIDE BAR GRAPH
    ################################################################################################
    def setEnableBarGraph(self, enable = True):
    def setEnableBarGraph(self, enable=True):
        self.enableBarGraph = enable

        if not self.use_timer_event:
@@ -890,7 +903,7 @@ def setEnableBarGraph(self, enable = True):
    ################################################################################################
    # SHOW HIDE VALUE TEXT
    ################################################################################################
    def setEnableValueText(self, enable = True):
    def setEnableValueText(self, enable=True):
        self.enable_value_text = enable

        if not self.use_timer_event:
@@ -899,7 +912,7 @@ def setEnableValueText(self, enable = True):
    ################################################################################################
    # SHOW HIDE CENTER POINTER
    ################################################################################################
    def setEnableCenterPoint(self, enable = True):
    def setEnableCenterPoint(self, enable=True):
        self.enable_CenterPoint = enable

        if not self.use_timer_event:
@@ -908,7 +921,7 @@ def setEnableCenterPoint(self, enable = True):
    ################################################################################################
    # SHOW HIDE FILLED POLYGON
    ################################################################################################
    def setEnableScalePolygon(self, enable = True):
    def setEnableScalePolygon(self, enable=True):
        self.enable_filled_Polygon = enable

        if not self.use_timer_event:
@@ -917,17 +930,17 @@ def setEnableScalePolygon(self, enable = True):
    ################################################################################################
    # SHOW HIDE BIG SCALE
    ################################################################################################
    def setEnableBigScaleGrid(self, enable = True):
    def setEnableBigScaleGrid(self, enable=True):
        self.enable_big_scaled_marker = enable

        if not self.use_timer_event:
            self.update()


    ################################################################################################
    # SHOW HIDE FINE SCALE
    ################################################################################################
    def setEnableFineScaleGrid(self, enable = True):

    def setEnableFineScaleGrid(self, enable=True):
        self.enable_fine_scaled_marker = enable

        if not self.use_timer_event:
@@ -1041,7 +1054,7 @@ def get_value_max(self):
    ################################################################################################
    # CREATE PIE
    ################################################################################################
    def create_polygon_pie(self, outer_radius, inner_raduis, start, lenght, bar_graph = True):
    def create_polygon_pie(self, outer_radius, inner_raduis, start, lenght, bar_graph=True):
        polygon_pie = QPolygonF()
        # start = self.scale_angle_start_value
        # start = 0
@@ -1059,19 +1072,22 @@ def create_polygon_pie(self, outer_radius, inner_raduis, start, lenght, bar_grap
        # todo enable/disable bar graf here
        if not self.enableBarGraph and bar_graph:
            # float_value = ((lenght / (self.maxValue - self.minValue)) * (self.value - self.minValue))
            lenght = int(round((lenght / (self.maxValue - self.minValue)) * (self.value - self.minValue)))
            lenght = int(
                round((lenght / (self.maxValue - self.minValue)) * (self.value - self.minValue)))
            # print("f: %s, l: %s" %(float_value, lenght))
            pass

        # mymax = 0

        for i in range(lenght+1):                                              # add the points of polygon
        # add the points of polygon
        for i in range(lenght + 1):
            t = w * i + start - self.angle_offset
            x = outer_radius * math.cos(math.radians(t))
            y = outer_radius * math.sin(math.radians(t))
            polygon_pie.append(QPointF(x, y))
        # create inner circle line from "start + lenght"-angle to "start"-angle
        for i in range(lenght+1):                                              # add the points of polygon
        # add the points of polygon
        for i in range(lenght + 1):
            # print("2 " + str(i))
            t = w * (lenght - i) + start - self.angle_offset
            x = inner_raduis * math.cos(math.radians(t))
@@ -1087,7 +1103,8 @@ def draw_filled_polygon(self, outline_pen_with=0):
            painter_filled_polygon = QPainter(self)
            painter_filled_polygon.setRenderHint(QPainter.Antialiasing)
            # Koordinatenursprung in die Mitte der Flaeche legen
            painter_filled_polygon.translate(self.width() / 2, self.height() / 2)
            painter_filled_polygon.translate(
                self.width() / 2, self.height() / 2)

            painter_filled_polygon.setPen(Qt.NoPen)

@@ -1096,11 +1113,14 @@ def draw_filled_polygon(self, outline_pen_with=0):
                painter_filled_polygon.setPen(self.pen)

            colored_scale_polygon = self.create_polygon_pie(
                ((self.widget_diameter / 2) - (self.pen.width() / 2)) * self.gauge_color_outer_radius_factor,
                (((self.widget_diameter / 2) - (self.pen.width() / 2)) * self.gauge_color_inner_radius_factor),
                ((self.widget_diameter / 2) - (self.pen.width() / 2)) *
                self.gauge_color_outer_radius_factor,
                (((self.widget_diameter / 2) - (self.pen.width() / 2))
                 * self.gauge_color_inner_radius_factor),
                self.scale_angle_start_value, self.scale_angle_size)

            gauge_rect = QRect(QPoint(0, 0), QSize(self.widget_diameter / 2 - 1, self.widget_diameter - 1))
            gauge_rect = QRect(QPoint(0, 0), QSize(
                int(self.widget_diameter / 2 - 1), int(self.widget_diameter - 1)))
            grad = QConicalGradient(QPointF(0, 0), - self.scale_angle_size - self.scale_angle_start_value +
                                    self.angle_offset - 1)

@@ -1115,7 +1135,6 @@ def draw_filled_polygon(self, outline_pen_with=0):
            # grad.setStyle(Qt.Dense6Pattern)
            # painter_filled_polygon.setBrush(self.brush)
            painter_filled_polygon.setBrush(grad)


            painter_filled_polygon.drawPolygon(colored_scale_polygon)
            # return painter_filled_polygon
@@ -1140,11 +1159,13 @@ def draw_big_scaled_marker(self):

        my_painter.rotate(self.scale_angle_start_value - self.angle_offset)
        steps_size = (float(self.scale_angle_size) / float(self.scalaCount))
        scale_line_outer_start = self.widget_diameter/2
        scale_line_lenght = (self.widget_diameter / 2) - (self.widget_diameter / 20)
        scale_line_outer_start = self.widget_diameter // 2
        scale_line_lenght = int((self.widget_diameter / 2) -
                                (self.widget_diameter / 20))
        # print(stepszize)
        for i in range(self.scalaCount+1):
            my_painter.drawLine(scale_line_lenght, 0, scale_line_outer_start, 0)
        for i in range(self.scalaCount + 1):
            my_painter.drawLine(scale_line_lenght, 0,
                                scale_line_outer_start, 0)
            my_painter.rotate(steps_size)

    def create_scale_marker_values_text(self):
@@ -1164,24 +1185,27 @@ def create_scale_marker_values_text(self):
        painter.setPen(pen_shadow)

        text_radius_factor = 0.8
        text_radius = self.widget_diameter/2 * text_radius_factor
        text_radius = self.widget_diameter / 2 * text_radius_factor

        scale_per_div = int((self.maxValue - self.minValue) / self.scalaCount)

        angle_distance = (float(self.scale_angle_size) / float(self.scalaCount))
        angle_distance = (float(self.scale_angle_size) /
                          float(self.scalaCount))
        for i in range(self.scalaCount + 1):
            # text = str(int((self.maxValue - self.minValue) / self.scalaCount * i))
            text = str(int(self.minValue + scale_per_div * i))
            w = fm.width(text) + 1
            h = fm.height()
            painter.setFont(QFont(self.scale_fontname, self.scale_fontsize, QFont.Bold))
            angle = angle_distance * i + float(self.scale_angle_start_value - self.angle_offset)
            painter.setFont(QFont(self.scale_fontname,
                            self.scale_fontsize, QFont.Bold))
            angle = angle_distance * i + \
                float(self.scale_angle_start_value - self.angle_offset)
            x = text_radius * math.cos(math.radians(angle))
            y = text_radius * math.sin(math.radians(angle))
            # print(w, h, x, y, text)

            text = [x - int(w/2), y - int(h/2), int(w), int(h), Qt.AlignCenter, text]
            painter.drawText(text[0], text[1], text[2], text[3], text[4], text[5])
            painter.drawText(int(x - w / 2), int(y - h / 2), int(w),
                             int(h), Qt.AlignCenter, text)
        # painter.restore()

    ################################################################################################
@@ -1197,11 +1221,14 @@ def create_fine_scaled_marker(self):

        my_painter.setPen(self.fineScaleColor)
        my_painter.rotate(self.scale_angle_start_value - self.angle_offset)
        steps_size = (float(self.scale_angle_size) / float(self.scalaCount * self.scala_subdiv_count))
        scale_line_outer_start = self.widget_diameter/2
        scale_line_lenght = (self.widget_diameter / 2) - (self.widget_diameter / 40)
        for i in range((self.scalaCount * self.scala_subdiv_count)+1):
            my_painter.drawLine(scale_line_lenght, 0, scale_line_outer_start, 0)
        steps_size = (float(self.scale_angle_size) /
                      float(self.scalaCount * self.scala_subdiv_count))
        scale_line_outer_start = self.widget_diameter // 2
        scale_line_lenght = int(
            (self.widget_diameter / 2) - (self.widget_diameter / 40))
        for i in range((self.scalaCount * self.scala_subdiv_count) + 1):
            my_painter.drawLine(scale_line_lenght, 0,
                                scale_line_outer_start, 0)
            my_painter.rotate(steps_size)

    ################################################################################################
@@ -1231,31 +1258,35 @@ def create_values_text(self):
        text = str(int(self.value))
        w = fm.width(text) + 1
        h = fm.height()
        painter.setFont(QFont(self.value_fontname, self.value_fontsize, QFont.Bold))
        painter.setFont(QFont(self.value_fontname,
                        self.value_fontsize, QFont.Bold))

        # Mitte zwischen Skalenstart und Skalenende:
        # Skalenende = Skalenanfang - 360 + Skalenlaenge
        # Skalenmitte = (Skalenende - Skalenanfang) / 2 + Skalenanfang
        angle_end = float(self.scale_angle_start_value + self.scale_angle_size - 360)
        angle = (angle_end - self.scale_angle_start_value) / 2 + self.scale_angle_start_value
        angle_end = float(self.scale_angle_start_value +
                          self.scale_angle_size - 360)
        angle = (angle_end - self.scale_angle_start_value) / \
            2 + self.scale_angle_start_value

        x = text_radius * math.cos(math.radians(angle))
        y = text_radius * math.sin(math.radians(angle))
        # print(w, h, x, y, text)
        text = [x - int(w/2), y - int(h/2), int(w), int(h), Qt.AlignCenter, text]
        painter.drawText(text[0], text[1], text[2], text[3], text[4], text[5])

        painter.drawText(int(x - w / 2), int(y - h / 2), int(w),
                         int(h), Qt.AlignCenter, text)

    ################################################################################################
    # UNITS TEXT
    ################################################################################################

    def create_units_text(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        # painter.setRenderHint(QPainter.Antialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        font = QFont(self.value_fontname, int(self.value_fontsize / 2.5), QFont.Bold)
        font = QFont(self.value_fontname, int(
            self.value_fontsize / 2.5), QFont.Bold)
        fm = QFontMetrics(font)

        pen_shadow = QPen()
@@ -1268,22 +1299,24 @@ def create_units_text(self):
        text = str(self.units)
        w = fm.width(text) + 1
        h = fm.height()
        painter.setFont(QFont(self.value_fontname, int(self.value_fontsize / 2.5), QFont.Bold))
        painter.setFont(QFont(self.value_fontname, int(
            self.value_fontsize / 2.5), QFont.Bold))


        angle_end = float(self.scale_angle_start_value + self.scale_angle_size + 180)
        angle = (angle_end - self.scale_angle_start_value) / 2 + self.scale_angle_start_value
        angle_end = float(self.scale_angle_start_value +
                          self.scale_angle_size + 180)
        angle = (angle_end - self.scale_angle_start_value) / \
            2 + self.scale_angle_start_value

        x = text_radius * math.cos(math.radians(angle))
        y = text_radius * math.sin(math.radians(angle))
        # print(w, h, x, y, text)
        text = [x - int(w/2), y - int(h/2), int(w), int(h), Qt.AlignCenter, text]
        painter.drawText(text[0], text[1], text[2], text[3], text[4], text[5])

        painter.drawText(int(x - w / 2), int(y - h / 2), int(w),
                         int(h), Qt.AlignCenter, text)

    ################################################################################################
    # CENTER POINTER
    ################################################################################################

    def draw_big_needle_center_point(self, diameter=30):
        painter = QPainter(self)
        # painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)
@@ -1298,12 +1331,11 @@ def draw_big_needle_center_point(self, diameter=30):
        # diameter = diameter # self.widget_diameter/6
        # painter.drawEllipse(int(-diameter / 2), int(-diameter / 2), int(diameter), int(diameter))


        # create_polygon_pie(self, outer_radius, inner_raduis, start, lenght)
        colored_scale_polygon = self.create_polygon_pie(
                ((self.widget_diameter / 8) - (self.pen.width() / 2)),
                0,
                self.scale_angle_start_value, 360, False)
            ((self.widget_diameter / 8) - (self.pen.width() / 2)),
            0,
            self.scale_angle_start_value, 360, False)

        # 150.0 0.0 131 360

@@ -1333,24 +1365,23 @@ def draw_outer_circle(self, diameter=30):
        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(Qt.NoPen)
        colored_scale_polygon = self.create_polygon_pie(
                ((self.widget_diameter / 2) - (self.pen.width())),
                (self.widget_diameter / 6),
                self.scale_angle_start_value / 10, 360, False)
            ((self.widget_diameter / 2) - (self.pen.width())),
            (self.widget_diameter / 6),
            self.scale_angle_start_value / 10, 360, False)

        radialGradient = QRadialGradient(QPointF(0, 0), self.width())

        for eachcolor in self.outer_circle_bg:
            radialGradient.setColorAt(eachcolor[0], eachcolor[1])


        painter.setBrush(radialGradient)

        painter.drawPolygon(colored_scale_polygon)


    ################################################################################################
    # NEEDLE POINTER
    ################################################################################################

    def draw_needle(self):
        painter = QPainter(self)
        # painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)
@@ -1416,8 +1447,8 @@ def paintEvent(self, event):

        # Draw Center Point
        if self.enable_CenterPoint:
            self.draw_big_needle_center_point(diameter=(self.widget_diameter / 6))

            self.draw_big_needle_center_point(
                diameter=(self.widget_diameter / 6))

    ###############################################################################################
    # MOUSE EVENTS
@@ -1443,23 +1474,24 @@ def mouseReleaseEvent(self, QMouseEvent):
        pass

    ########################################################################
    ## MOUSE LEAVE EVENT
    # MOUSE LEAVE EVENT
    ########################################################################
    def leaveEvent(self, event):
        self.NeedleColor = self.NeedleColorReleased
        self.update() 
        self.update()

    def mouseMoveEvent(self, event):
        x, y = event.x() - (self.width() / 2), event.y() - (self.height() / 2)
        # print(event.x(), event.y(), self.width(), self.height())
        if not x == 0: 
        if not x == 0:
            angle = math.atan2(y, x) / math.pi * 180
            # winkellaenge der anzeige immer positiv 0 - 360deg
            # min wert + umskalierter wert
            value = (float(math.fmod(angle - self.scale_angle_start_value + 720, 360)) / \
            value = (float(math.fmod(angle - self.scale_angle_start_value + 720, 360)) /
                     (float(self.scale_angle_size) / float(self.maxValue - self.minValue))) + self.minValue
            temp = value
            fmod = float(math.fmod(angle - self.scale_angle_start_value + 720, 360))
            fmod = float(
                math.fmod(angle - self.scale_angle_start_value + 720, 360))
            state = 0
            if (self.value - (self.maxValue - self.minValue) * self.valueNeedleSnapzone) <= \
                    value <= \
@@ -1481,13 +1513,12 @@ def mouseMoveEvent(self, event):
                    self.last_value = self.maxValue
                    self.valueChanged.emit(int(value))


                else:
                    state = 3
                    self.last_value = value
                    self.valueChanged.emit(int(value))

                self.updateValue(value)            
                self.updateValue(value)

################################################################################################
# END ==>