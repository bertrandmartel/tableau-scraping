import json
from re import T

emptyData = {"secondaryInfo": ""}
dataWithoutViz = {"secondaryInfo": {"presModelMap": {}}}
dataWithoutPres1 = {"secondaryInfo": {"presModelMap": {"vizData": {}}}}
dataWithoutMapPresModel = {
    "secondaryInfo": {"presModelMap": {"vizData": {"presModelHolder": {}}}}
}
dataWithoutMapPres2 = {
    "secondaryInfo": {
        "presModelMap": {
            "vizData": {"presModelHolder": {"genPresModelMapPresModel": {}}}
        }
    }
}

noWorksheet = {
    "secondaryInfo": {
        "presModelMap": {
            "vizData": {
                "presModelHolder": {"genPresModelMapPresModel": {"presModelMap": {}}}
            }
        }
    }
}

dataWithoutPresModelWithDictionary = {
    "secondaryInfo": {
        "presModelMap": {
            "dataDictionary": {
                "presModelHolder": {
                    "genDataDictionaryPresModel": {
                        "dataSegments": {
                            "0": {
                                "dataColumns": [
                                    {
                                        "dataType": "cstring",
                                        "dataValues": ["1", "2", "3", "4", "5", "6"],
                                    },
                                    {"dataType": "real",
                                        "dataValues": [1, 2, 3, 4, 5]},
                                ]
                            },
                            "1": {
                                "dataColumns": [
                                    {
                                        "dataType": "cstring",
                                        "dataValues": ["7", "8", "9"],
                                    }
                                ]
                            },
                        }
                    }
                }
            }
        }
    }
}

data = {
    "secondaryInfo": {
        "presModelMap": {
            "vizData": {
                "presModelHolder": {
                    "genPresModelMapPresModel": {
                        "presModelMap": {
                            "[WORKSHEET1]": {
                                "presModelHolder": {
                                    "genVizDataPresModel": {
                                        "paneColumnsData": {
                                            "paneColumnsList": [
                                                {
                                                    "vizPaneColumns": [
                                                        {
                                                            "tupleIds": [],
                                                            "valueIndices": [
                                                                1,
                                                                2,
                                                                3,
                                                                4,
                                                            ],
                                                            "aliasIndices": [],
                                                        },
                                                        {
                                                            "tupleIds": [],
                                                            "valueIndices": [],
                                                            "aliasIndices": [
                                                                -6,
                                                                -7,
                                                                -8,
                                                                -9,
                                                            ],
                                                        },
                                                    ]
                                                }
                                            ],
                                            "vizDataColumns": [
                                                {
                                                    "fieldCaption": "[FIELD1]",
                                                    "dataType": "cstring",
                                                    "paneIndices": [0],
                                                    "columnIndices": [0],
                                                    "isAutoSelect": True,
                                                },
                                                {
                                                    "fieldCaption": "[FIELD2]",
                                                    "dataType": "cstring",
                                                    "paneIndices": [0],
                                                    "columnIndices": [1],
                                                },
                                            ],
                                        }
                                    }
                                }
                            },
                            "[WORKSHEET2]": {
                                "presModelHolder": {"genVizDataPresModel": {}}
                            },
                        }
                    }
                }
            },
            "dataDictionary": {
                "presModelHolder": {
                    "genDataDictionaryPresModel": {
                        "dataSegments": {
                            "0": {
                                "dataColumns": [
                                    {
                                        "dataType": "cstring",
                                        "dataValues": ["1", "2", "3", "4", "5", "6"],
                                    },
                                    {"dataType": "real",
                                        "dataValues": [1, 2, 3, 4, 5]},
                                ]
                            },
                            "1": {
                                "dataColumns": [
                                    {
                                        "dataType": "cstring",
                                        "dataValues": ["7", "8", "9"],
                                    }
                                ]
                            },
                        }
                    }
                }
            },
        }
    }
}

dataWithTupleIds = {
    "secondaryInfo": {
        "presModelMap": {
            "vizData": {
                "presModelHolder": {
                    "genPresModelMapPresModel": {
                        "presModelMap": {
                            "[WORKSHEET1]": {
                                "presModelHolder": {
                                    "genVizDataPresModel": {
                                        "paneColumnsData": {
                                            "paneColumnsList": [
                                                {
                                                    "vizPaneColumns": [
                                                        {
                                                            "tupleIds": [
                                                                2,
                                                                4,
                                                                6,
                                                                8,
                                                            ],
                                                            "valueIndices": [],
                                                            "aliasIndices": [],
                                                        }, {
                                                            "tupleIds": [],
                                                            "valueIndices": [
                                                                1,
                                                                2,
                                                                3,
                                                                4,
                                                            ],
                                                            "aliasIndices": [],
                                                        },
                                                        {
                                                            "tupleIds": [],
                                                            "valueIndices": [],
                                                            "aliasIndices": [
                                                                -6,
                                                                -7,
                                                                -8,
                                                                -9,
                                                            ],
                                                        },
                                                    ]
                                                }
                                            ],
                                            "vizDataColumns": [
                                                {
                                                    "fn": "[system:visual].[tuple_id]",
                                                    "paneIndices": [0],
                                                    "columnIndices": [0],
                                                },
                                                {
                                                    "fieldCaption": "[FIELD1]",
                                                    "dataType": "cstring",
                                                    "paneIndices": [0],
                                                    "columnIndices": [1],
                                                    "isAutoSelect": True,
                                                },
                                                {
                                                    "fieldCaption": "[FIELD2]",
                                                    "dataType": "cstring",
                                                    "paneIndices": [0],
                                                    "columnIndices": [2],
                                                },
                                            ],
                                        }
                                    }
                                }
                            },
                            "[WORKSHEET2]": {
                                "presModelHolder": {"genVizDataPresModel": {}}
                            },
                        }
                    }
                }
            },
            "dataDictionary": {
                "presModelHolder": {
                    "genDataDictionaryPresModel": {
                        "dataSegments": {
                            "0": {
                                "dataColumns": [
                                    {
                                        "dataType": "cstring",
                                        "dataValues": ["1", "2", "3", "4", "5", "6"],
                                    },
                                    {"dataType": "real",
                                        "dataValues": [1, 2, 3, 4, 5]},
                                ]
                            },
                            "1": {
                                "dataColumns": [
                                    {
                                        "dataType": "cstring",
                                        "dataValues": ["7", "8", "9"],
                                    }
                                ]
                            },
                        }
                    }
                }
            },
        }
    }
}

emptyValues = {
    "secondaryInfo": {
        "presModelMap": {
            "vizData": {
                "presModelHolder": {
                    "genPresModelMapPresModel": {
                        "presModelMap": {
                            "[WORKSHEET1]": {
                                "presModelHolder": {
                                    "genVizDataPresModel": {
                                        "paneColumnsData": {
                                            "paneColumnsList": [
                                                {
                                                    "vizPaneColumns": [
                                                        {
                                                            "tupleIds": [],
                                                            "valueIndices": [],
                                                            "aliasIndices": [],
                                                        },
                                                        {
                                                            "tupleIds": [],
                                                            "valueIndices": [],
                                                            "aliasIndices": [],
                                                        },
                                                    ]
                                                }
                                            ],
                                            "vizDataColumns": [
                                                {
                                                    "fieldCaption": "[FIELD1]",
                                                    "dataType": "cstring",
                                                    "paneIndices": [0],
                                                    "columnIndices": [0],
                                                    "isAutoSelect": True,
                                                },
                                                {
                                                    "fieldCaption": "[FIELD2]",
                                                    "dataType": "cstring",
                                                    "paneIndices": [0],
                                                    "columnIndices": [1],
                                                },
                                            ],
                                        }
                                    }
                                }
                            },
                            "[WORKSHEET2]": {
                                "presModelHolder": {"genVizDataPresModel": {}}
                            },
                        }
                    }
                }
            },
            "dataDictionary": {
                "presModelHolder": {
                    "genDataDictionaryPresModel": {
                        "dataSegments": {
                            "0": {
                                "dataColumns": [
                                    {"dataType": "cstring", "dataValues": []},
                                    {"dataType": "real", "dataValues": []},
                                ]
                            },
                            "1": {
                                "dataColumns": [
                                    {"dataType": "cstring", "dataValues": []}
                                ]
                            },
                        }
                    }
                }
            },
        }
    }
}

vqlCmdResponseEmptyValues = {
    "vqlCmdResponse": {
        "layoutStatus": {
            "applicationPresModel": {
                "workbookPresModel": {
                    "dashboardPresModel": {
                        "zones": {
                            "0": {
                                "worksheet": "[WORKSHEET1]",
                                "presModelHolder": {"visual": {"vizData": {}}},
                            },
                            "1": {
                                "worksheet": "[WORKSHEET2]",
                                "presModelHolder": {"visual": {"vizData": {}}},
                            },
                        }
                    }
                },
                "dataDictionary": {
                    "dataSegments": {
                        "0": {
                            "dataColumns": [
                                {
                                    "dataType": "cstring",
                                    "dataValues": ["1", "2", "3", "4", "5", "6"],
                                },
                                {"dataType": "real",
                                    "dataValues": [1, 2, 3, 4, 5]},
                            ]
                        },
                        "1": {
                            "dataColumns": [
                                {"dataType": "cstring",
                                    "dataValues": ["7", "8", "9"]}
                            ]
                        },
                    }
                },
            }
        }
    }
}

vqlCmdResponse = {
    "vqlCmdResponse": {
        "layoutStatus": {
            "applicationPresModel": {
                "workbookPresModel": {
                    "dashboardPresModel": {
                        "zones": {
                            "0": {
                                "worksheet": "[WORKSHEET1]",
                                "presModelHolder": {
                                    "visual": {
                                        "vizData": {
                                            "paneColumnsData": {
                                                "paneColumnsList": [
                                                    {
                                                        "vizPaneColumns": [
                                                            {
                                                                "tupleIds": [],
                                                                "valueIndices": [
                                                                    1,
                                                                    2,
                                                                    3,
                                                                    4,
                                                                ],
                                                                "aliasIndices": [],
                                                            },
                                                            {
                                                                "tupleIds": [],
                                                                "valueIndices": [],
                                                                "aliasIndices": [
                                                                    -6,
                                                                    -7,
                                                                    -8,
                                                                    -9,
                                                                ],
                                                            },
                                                        ]
                                                    }
                                                ],
                                                "vizDataColumns": [
                                                    {
                                                        "fieldCaption": "[FIELD1]",
                                                        "dataType": "cstring",
                                                        "paneIndices": [0],
                                                        "columnIndices": [0],
                                                        "isAutoSelect": True
                                                    },
                                                    {
                                                        "fieldCaption": "[FIELD2]",
                                                        "dataType": "cstring",
                                                        "paneIndices": [0],
                                                        "columnIndices": [1],
                                                    },
                                                ],
                                            }
                                        }
                                    },
                                    "parameterControl": {
                                        "fieldCaption": "[INPUT_NAME1]",
                                        "parameterName": "[Parameters].[Parameter 1]",
                                        "formattedValues": [
                                            "select1",
                                            "select2",
                                            "select3",
                                        ],
                                    },
                                },
                            },
                            "1": {
                                "worksheet": "[WORKSHEET2]",
                                "presModelHolder": {
                                    "visual": {
                                        "vizData": {},
                                    },
                                    "parameterControl": {
                                        "fieldCaption": "[INPUT_NAME2]",
                                        "parameterName": "[Parameters].[Parameter 1]",
                                        "formattedValues": [
                                            "select4",
                                            "select5",
                                            "select6",
                                        ],
                                    },
                                },
                            },
                        }
                    }
                },
                "dataDictionary": {
                    "dataSegments": {
                        "0": {
                            "dataColumns": [
                                {
                                    "dataType": "cstring",
                                    "dataValues": ["1", "2", "3", "4", "5", "6"],
                                },
                                {"dataType": "real",
                                    "dataValues": [1, 2, 3, 4, 5]},
                            ]
                        },
                        "1": {
                            "dataColumns": [
                                {"dataType": "cstring",
                                    "dataValues": ["7", "8", "9"]}
                            ]
                        },
                    }
                },
            }
        }
    }
}

vqlCmdResponseWithTupleIds = {
    "vqlCmdResponse": {
        "layoutStatus": {
            "applicationPresModel": {
                "workbookPresModel": {
                    "dashboardPresModel": {
                        "zones": {
                            "0": {
                                "worksheet": "[WORKSHEET1]",
                                "presModelHolder": {
                                    "visual": {
                                        "vizData": {
                                            "paneColumnsData": {
                                                "paneColumnsList": [
                                                    {
                                                        "vizPaneColumns": [
                                                            {
                                                                "tupleIds": [
                                                                    2,
                                                                    4,
                                                                    6,
                                                                    8,
                                                                ],
                                                                "valueIndices": [],
                                                                "aliasIndices": [],
                                                            },
                                                            {
                                                                "tupleIds": [],
                                                                "valueIndices": [
                                                                    1,
                                                                    2,
                                                                    3,
                                                                    4,
                                                                ],
                                                                "aliasIndices": [],
                                                            },
                                                            {
                                                                "tupleIds": [],
                                                                "valueIndices": [],
                                                                "aliasIndices": [
                                                                    -6,
                                                                    -7,
                                                                    -8,
                                                                    -9,
                                                                ],
                                                            },
                                                        ]
                                                    }
                                                ],
                                                "vizDataColumns": [
                                                    {
                                                        "fn": "[system:visual].[tuple_id]",
                                                        "paneIndices": [0],
                                                        "columnIndices": [0],
                                                    },
                                                    {
                                                        "fieldCaption": "[FIELD1]",
                                                        "dataType": "cstring",
                                                        "paneIndices": [0],
                                                        "columnIndices": [1],
                                                        "isAutoSelect": True
                                                    },
                                                    {
                                                        "fieldCaption": "[FIELD2]",
                                                        "dataType": "cstring",
                                                        "paneIndices": [0],
                                                        "columnIndices": [2],
                                                    },
                                                ],
                                            }
                                        }
                                    },
                                    "parameterControl": {
                                        "fieldCaption": "[INPUT_NAME1]",
                                        "parameterName": "[Parameters].[Parameter 1]",
                                        "formattedValues": [
                                            "select1",
                                            "select2",
                                            "select3",
                                        ],
                                    },
                                },
                            },
                            "1": {
                                "worksheet": "[WORKSHEET2]",
                                "presModelHolder": {
                                    "visual": {
                                        "vizData": {},
                                    },
                                    "parameterControl": {
                                        "fieldCaption": "[INPUT_NAME2]",
                                        "parameterName": "[Parameters].[Parameter 1]",
                                        "formattedValues": [
                                            "select4",
                                            "select5",
                                            "select6",
                                        ],
                                    },
                                },
                            },
                        }
                    }
                },
                "dataDictionary": {
                    "dataSegments": {
                        "0": {
                            "dataColumns": [
                                {
                                    "dataType": "cstring",
                                    "dataValues": ["1", "2", "3", "4", "5", "6"],
                                },
                                {"dataType": "real",
                                    "dataValues": [1, 2, 3, 4, 5]},
                            ]
                        },
                        "1": {
                            "dataColumns": [
                                {"dataType": "cstring",
                                    "dataValues": ["7", "8", "9"]}
                            ]
                        },
                    }
                },
            }
        }
    }
}

vqlCmdResponseDictionaryEmpty = {
    "vqlCmdResponse": {
        "layoutStatus": {
            "applicationPresModel": {
                "workbookPresModel": {
                    "dashboardPresModel": {
                        "zones": {
                            "0": {
                                "worksheet": "[WORKSHEET1]",
                                "presModelHolder": {
                                    "visual": {
                                        "vizData": {
                                            "paneColumnsData": {
                                                "paneColumnsList": [
                                                    {
                                                        "vizPaneColumns": [
                                                            {
                                                                "tupleIds": [],
                                                                "valueIndices": [],
                                                                "aliasIndices": [],
                                                            },
                                                            {
                                                                "tupleIds": [],
                                                                "valueIndices": [],
                                                                "aliasIndices": [],
                                                            },
                                                        ]
                                                    }
                                                ],
                                                "vizDataColumns": [
                                                    {
                                                        "fieldCaption": "[FIELD1]",
                                                        "dataType": "cstring",
                                                        "paneIndices": [0],
                                                        "columnIndices": [0],
                                                        "isAutoSelect": True
                                                    },
                                                    {
                                                        "fieldCaption": "[FIELD2]",
                                                        "dataType": "cstring",
                                                        "paneIndices": [0],
                                                        "columnIndices": [1],
                                                    },
                                                ],
                                            }
                                        }
                                    },
                                    "parameterControl": {
                                        "fieldCaption": "[INPUT_NAME1]",
                                        "parameterName": "[Parameters].[Parameter 1]",
                                        "formattedValues": [
                                            "select1",
                                            "select2",
                                            "select3",
                                        ],
                                    },
                                },
                            },
                            "1": {
                                "worksheet": "[WORKSHEET2]",
                                "presModelHolder": {
                                    "visual": {
                                        "vizData": {},
                                    },
                                    "parameterControl": {
                                        "fieldCaption": "[INPUT_NAME2]",
                                        "parameterName": "[Parameters].[Parameter 1]",
                                        "formattedValues": [
                                            "select4",
                                            "select5",
                                            "select6",
                                        ],
                                    },
                                },
                            },
                        }
                    }
                },
                "dataDictionary": {
                    "dataSegments": {
                        "0": {
                            "dataColumns": [
                                {
                                    "dataType": "cstring",
                                    "dataValues": [],
                                },
                                {"dataType": "real", "dataValues": []},
                            ]
                        },
                        "1": {
                            "dataColumns": [
                                {"dataType": "cstring", "dataValues": []}
                            ]
                        },
                    }
                },
            }
        }
    }
}

storyPointsCmdResponse = {
    "vqlCmdResponse": {
        "layoutStatus": {
            "applicationPresModel": {
                "workbookPresModel": {
                    "dashboardPresModel": {
                        "zones": {
                            "2": {
                                "worksheet": "[WORKSHEET1]",
                                "presModelHolder": {
                                    "visual": {
                                        "filtersJson": json.dumps([{
                                            "table": {
                                                "schema": [{
                                                    "caption": "FILTER_1",
                                                    "ordinal": 0,
                                                    "name": ["FILTER", "FILTER_1"]
                                                }],
                                                "tuples": [{
                                                    "t": [{
                                                        "v": "FITLTER_VALUE_1"
                                                    }]
                                                }, {
                                                    "t": [{
                                                        "v": "FITLTER_VALUE_2"
                                                    }]
                                                }, {
                                                    "t": [{
                                                        "v": "FITLTER_VALUE_3"
                                                    }]
                                                }]
                                            }
                                        }])
                                    }
                                }
                            },
                            "3": {
                                "presModelHolder": {
                                    "flipboard": {
                                        "storyPoints": {
                                            "1": {
                                                "dashboardPresModel": {
                                                    "zones": {
                                                        "0": {
                                                            "worksheet": "[WORKSHEET1]",
                                                            "presModelHolder": {"visual": {"vizData": {
                                                                "paneColumnsData": {
                                                                    "paneColumnsList": [
                                                                        {
                                                                            "vizPaneColumns": [
                                                                                {
                                                                                    "tupleIds": [],
                                                                                    "valueIndices": [
                                                                                        1,
                                                                                        2,
                                                                                        3,
                                                                                        4,
                                                                                    ],
                                                                                    "aliasIndices": [],
                                                                                },
                                                                                {
                                                                                    "tupleIds": [],
                                                                                    "valueIndices": [],
                                                                                    "aliasIndices": [
                                                                                        -6,
                                                                                        -7,
                                                                                        -8,
                                                                                        -9,
                                                                                    ],
                                                                                },
                                                                            ]
                                                                        }
                                                                    ],
                                                                    "vizDataColumns": [
                                                                        {
                                                                            "fieldCaption": "[FIELD1]",
                                                                            "dataType": "cstring",
                                                                            "paneIndices": [0],
                                                                            "columnIndices": [0],
                                                                            "isAutoSelect": True,
                                                                        },
                                                                        {
                                                                            "fieldCaption": "[FIELD2]",
                                                                            "dataType": "cstring",
                                                                            "paneIndices": [0],
                                                                            "columnIndices": [1],
                                                                            "isAutoSelect": True
                                                                        },
                                                                    ]
                                                                }
                                                            }}},
                                                        },
                                                        "1": {
                                                            "presModelHolder": {
                                                                "parameterControl": {
                                                                    "fieldCaption": "[INPUT_NAME1]",
                                                                    "parameterName": "[Parameters].[Parameter 1]",
                                                                    "formattedValues": [
                                                                        "select1",
                                                                        "select2",
                                                                        "select3",
                                                                    ],
                                                                }
                                                            }
                                                        },
                                                        "2": {
                                                            "presModelHolder": {
                                                                "parameterControl": {
                                                                    "fieldCaption": "[INPUT_NAME2]",
                                                                    "parameterName": "[Parameters].[Parameter 1]",
                                                                    "formattedValues": [
                                                                        "select4",
                                                                        "select5",
                                                                        "select6",
                                                                    ],
                                                                }
                                                            }
                                                        },
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "dataDictionary": {
                    "dataSegments": {
                        "0": {
                            "dataColumns": [
                                {
                                    "dataType": "cstring",
                                    "dataValues": ["1", "2", "3", "4", "5", "6"],
                                },
                                {"dataType": "real",
                                    "dataValues": [1, 2, 3, 4, 5]},
                            ]
                        },
                        "1": {
                            "dataColumns": [
                                {"dataType": "cstring",
                                    "dataValues": ["7", "8", "9"]}
                            ]
                        },
                    }
                },
            }
        }
    }
}

tooltipCmdResponse = {
    "vqlCmdResponse": {
        "cmdResultList": [{
            "commandName": "tabsrv:render-tooltip-server",
            "commandReturn": {
                "tooltipText": json.dumps({
                    "htmlTooltip": "<div></div>"
                })
            }
        }],
        "layoutStatus": {

        }
    }
}

storyPointsInfo = {
    "sheetName": "[SHEET_NAME]",
    "worldUpdate": {
        "applicationPresModel": {
            "workbookPresModel": {
                "dashboardPresModel": {
                    "zones": {
                        "2": {
                            "worksheet": "[WORKSHEET1]",
                            "presModelHolder": {
                                "visual": {
                                    "filtersJson": json.dumps([{
                                        "table": {
                                            "schema": [{
                                                "caption": "FILTER_1",
                                                "ordinal": 0,
                                                "name": ["FILTER", "FILTER_1"]
                                            }],
                                            "tuples": [{
                                                "t": [{
                                                    "v": "FITLTER_VALUE_1"
                                                }]
                                            }, {
                                                "t": [{
                                                    "v": "FITLTER_VALUE_2"
                                                }]
                                            }, {
                                                "t": [{
                                                    "v": "FITLTER_VALUE_3"
                                                }]
                                            }]
                                        }
                                    }])
                                }
                            }
                        },
                        "3": {
                            "presModelHolder": {
                                "flipboard": {
                                    "storyPoints": {
                                        "1": {
                                            "dashboardPresModel": {
                                                "zones": {
                                                    "0": {
                                                        "worksheet": "[WORKSHEET1]",
                                                        "presModelHolder": {"visual": {"vizData": {
                                                            "paneColumnsData": {
                                                                "paneColumnsList": [
                                                                    {
                                                                        "vizPaneColumns": [
                                                                            {
                                                                                "tupleIds": [],
                                                                                "valueIndices": [
                                                                                    1,
                                                                                    2,
                                                                                    3,
                                                                                    4,
                                                                                ],
                                                                                "aliasIndices": [],
                                                                            },
                                                                            {
                                                                                "tupleIds": [],
                                                                                "valueIndices": [],
                                                                                "aliasIndices": [
                                                                                    -6,
                                                                                    -7,
                                                                                    -8,
                                                                                    -9,
                                                                                ],
                                                                            },
                                                                        ]
                                                                    }
                                                                ],
                                                                "vizDataColumns": [
                                                                    {
                                                                        "fieldCaption": "[FIELD1]",
                                                                        "dataType": "cstring",
                                                                        "paneIndices": [0],
                                                                        "columnIndices": [0],
                                                                        "isAutoSelect": True,
                                                                    },
                                                                    {
                                                                        "fieldCaption": "[FIELD2]",
                                                                        "dataType": "cstring",
                                                                        "paneIndices": [0],
                                                                        "columnIndices": [1],
                                                                        "isAutoSelect": True
                                                                    },
                                                                ]
                                                            }
                                                        }}},
                                                    },
                                                    "1": {
                                                        "presModelHolder": {
                                                            "parameterControl": {
                                                                "fieldCaption": "[INPUT_NAME1]",
                                                                "parameterName": "[Parameters].[Parameter 1]",
                                                                "formattedValues": [
                                                                    "select1",
                                                                    "select2",
                                                                    "select3",
                                                                ],
                                                            }
                                                        }
                                                    },
                                                    "2": {
                                                        "presModelHolder": {
                                                            "parameterControl": {
                                                                "fieldCaption": "[INPUT_NAME2]",
                                                                "parameterName": "[Parameters].[Parameter 1]",
                                                                "formattedValues": [
                                                                    "select4",
                                                                    "select5",
                                                                    "select6",
                                                                ],
                                                            }
                                                        }
                                                    },
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    },
}

info = {
    "sheetName": "[SHEET_NAME]",
    "worldUpdate": {
        "applicationPresModel": {
            "workbookPresModel": {
                "dashboardPresModel": {
                    "zones": {
                        "0": {
                            "presModelHolder": {
                                "parameterControl": {
                                    "fieldCaption": "[INPUT_NAME1]",
                                    "parameterName": "[Parameters].[Parameter 1]",
                                    "formattedValues": [
                                        "select1",
                                        "select2",
                                        "select3",
                                    ],
                                }
                            }
                        },
                        "1": {
                            "presModelHolder": {
                                "parameterControl": {
                                    "fieldCaption": "[INPUT_NAME2]",
                                    "parameterName": "[Parameters].[Parameter 1]",
                                    "formattedValues": [
                                        "select4",
                                        "select5",
                                        "select6",
                                    ],
                                }
                            }
                        },
                        "2": {
                            "worksheet": "[WORKSHEET1]",
                            "presModelHolder": {
                                "visual": {
                                    "filtersJson": json.dumps([{
                                        "table": {
                                            "schema": [{
                                                "caption": "FILTER_1",
                                                "ordinal": 0,
                                                "name": ["FILTER", "FILTER_1"]
                                            }],
                                            "tuples": [{
                                                "t": [{
                                                    "v": "FITLTER_VALUE_1"
                                                }]
                                            }, {
                                                "t": [{
                                                    "v": "FITLTER_VALUE_2"
                                                }]
                                            }, {
                                                "t": [{
                                                    "v": "FITLTER_VALUE_3"
                                                }]
                                            }]
                                        }
                                    }])
                                }
                            }
                        },
                    },
                    'viewIds': {
                        '[WORKSHEET1]': '12302628778901485932_5034431464735168763',
                    },
                },
                "sheetsInfo": [{
                    "sheet": "[WORKSHEET1]",
                    "isDashboard": False,
                    "isVisible": True,
                    "namesOfSubsheets": [],
                    "windowId":"{XXXXX}"
                }]
            }
        }
    },
}

tableauVizHtmlResponse = """
<div>
<textarea id="tsConfigContainer">
{
	"vizql_root": "test",
	"sessionid": "123456:123456",
	"sheetId": "SHEET/NAME"
}
</textarea>
</div>
"""

tableauDataResponse = """
433337;%s433337;%s
""" % (
    json.dumps(info),
    json.dumps(data),
)

tableauDataResponseWithTupleIds = """
433337;%s433337;%s
""" % (
    json.dumps(info),
    json.dumps(dataWithTupleIds),
)

tableauDataResponseWithStoryPoints = """
433337;%s433337;%s
""" % (
    json.dumps(storyPointsInfo),
    json.dumps(dataWithoutPresModelWithDictionary),
)

fakeUri = "https://public.tableau.com/example"

tableauSessionResponse = """
<html>
</html>
"""

tableauPlaceHolderData = """
<html>
    <div class="tableauPlaceholder">
        <param name="host_url" value="example.com"/>
        <param name="site_root" value="/site/root"/>
        <param name="name" value="/someurl"/>
    </div>
</html>
"""

tableauPlaceHolderDataWithTicket = """
<html>
    <div class="tableauPlaceholder">
        <param name="host_url" value="example.com"/>
        <param name="site_root" value="/site/root"/>
        <param name="name" value="/someurl"/>
        <param name="ticket" value="XXXXXXXXXXXXX"/>
    </div>
</html>
"""

tableauPlaceHolderDataEmpty = """
<html>
    <div class="tableauPlaceholder">
    </div>
</html>
"""

tableauDownloadableSummaryData = """
{
	"vqlCmdResponse": {
		"layoutStatus": {
		},
		"cmdResultList": [{
			"commandName": "tabdoc:get-summary-data",
			"commandReturn": {
				"underlyingDataTable": {
					"tableAlias": "",
					"tableName": "",
					"numRows": 896,
					"dataDictionary": {
						"dataSegments": {
							"0": {
								"dataColumns": [{
									"dataType": "real",
									"dataValues": [149, 158, 161, 163, 170, 169, 181, 190, 195, 206, 208, 217, 232, 245, 252, 255, 260, 267, 304, 300, 297, 307, 303, 315, 326, 330, 339, 362, 387, 392, 407, 415, 433, 463, 491, 493, 511, 544, 571, 605, 610, 625, 613, 637, 658, 666, 691, 712, 728, 729, 742, 767, 786, 811, 817, 823, 836, 849, 866, 868, 886, 887, 869, 860, 877, 882, 899, 947, 950, 937, 906, 902, 913, 894, 903, 890, 896, 931, 918, 925, 885, 909, 924, 934, 954, 943, 923, 927, 953, 935, 955, 999, 1011, 1005, 1012, 1030, 1043, 1047, 1076, 1065, 1083, 1121, 1132, 1124, 1154, 1176, 1148, 1162, 1199, 1258, 1273, 1271, 1270, 1285, 1328, 1358, 1402, 1423, 1412, 1454, 1459, 1481, 1516, 1506, 1522, 1503, 1500, 1534, 1551, 1543, 1584, 1558, 1544, 1527, 1562, 1546, 1560, 1621, 1614, 1523, 1550, 1580, 1570, 1536, 1501, 1492, 1426, 1436, 1428, 1475, 1424, 1408, 1392, 1357, 1344, 1321, 1292, 1276, 1250, 1224, 1222, 1187, 1129, 1160, 1166, 1126, 1095, 1045, 1088, 1068, 1098, 1040, 1009, 1029, 1007, 994, 952, 872, 850, 825, 795, 783, 718, 681]
								}, {
									"dataType": "cstring",
									"dataValues": ["[federated.05hfglv18oi9571bhp1mu1gb9wja].[sum:CURRENT_ICU_PATIENTS:qk]", "Total COVID-19 Patients in ICU", "6/16/2021", "6/15/2021", "6/14/2021", "6/13/2021", "6/12/2021", "6/11/2021", "6/10/2021", "6/9/2021", "6/8/2021", "6/7/2021", "6/6/2021", "6/5/2021", "6/4/2021", "6/3/2021", "6/2/2021", "6/1/2021", "5/31/2021", "5/30/2021", "5/29/2021", "5/28/2021", "5/27/2021", "5/26/2021", "5/25/2021", "5/24/2021", "5/23/2021", "5/22/2021", "5/21/2021", "5/20/2021", "5/19/2021", "5/18/2021", "5/17/2021", "5/16/2021", "5/15/2021", "5/14/2021", "5/13/2021", "5/12/2021", "5/11/2021", "5/10/2021", "5/9/2021", "5/8/2021", "5/7/2021", "5/6/2021", "5/5/2021", "5/4/2021", "5/3/2021", "5/2/2021", "5/1/2021", "4/30/2021", "4/29/2021", "4/28/2021", "4/27/2021", "4/26/2021", "4/25/2021", "4/24/2021", "4/23/2021", "4/22/2021", "4/21/2021", "4/20/2021", "4/19/2021", "4/18/2021", "4/17/2021", "4/16/2021", "4/15/2021", "4/14/2021", "4/13/2021", "4/12/2021", "4/11/2021", "4/10/2021", "4/9/2021", "4/8/2021", "4/7/2021", "4/6/2021", "4/5/2021", "4/4/2021", "4/3/2021", "4/2/2021", "4/1/2021", "3/31/2021", "3/30/2021", "3/29/2021", "3/28/2021", "3/27/2021", "3/26/2021", "3/25/2021", "3/24/2021", "3/23/2021", "3/22/2021", "3/21/2021", "3/20/2021", "3/19/2021", "3/18/2021", "3/17/2021", "3/16/2021", "3/15/2021", "3/14/2021", "3/13/2021", "3/12/2021", "3/11/2021", "3/10/2021", "3/9/2021", "3/8/2021", "3/7/2021", "3/6/2021", "3/5/2021", "3/4/2021", "3/3/2021", "3/2/2021", "3/1/2021", "2/28/2021", "2/27/2021", "2/26/2021", "2/25/2021", "2/24/2021", "2/23/2021", "2/22/2021", "2/21/2021", "2/20/2021", "2/19/2021", "2/18/2021", "2/17/2021", "2/16/2021", "2/15/2021", "2/14/2021", "2/13/2021", "2/12/2021", "2/11/2021", "2/10/2021", "2/9/2021", "2/8/2021", "2/7/2021", "2/6/2021", "2/5/2021", "2/4/2021", "2/3/2021", "2/2/2021", "2/1/2021", "1/31/2021", "1/30/2021", "1/29/2021", "1/28/2021", "1/27/2021", "1/26/2021", "1/25/2021", "1/24/2021", "1/23/2021", "1/22/2021", "1/21/2021", "1/20/2021", "1/19/2021", "1/18/2021", "1/17/2021", "1/16/2021", "1/15/2021", "1/14/2021", "1/13/2021", "1/12/2021", "1/11/2021", "1/10/2021", "1/9/2021", "1/8/2021", "1/7/2021", "1/6/2021", "1/5/2021", "1/4/2021", "1/3/2021", "1/2/2021", "1/1/2021", "12/31/2020", "12/30/2020", "12/29/2020", "12/28/2020", "12/27/2020", "12/26/2020", "12/25/2020", "12/24/2020", "12/23/2020", "12/22/2020", "12/21/2020", "12/20/2020", "12/19/2020", "12/18/2020", "12/17/2020", "12/16/2020", "12/15/2020", "12/14/2020", "12/13/2020", "12/12/2020", "12/11/2020", "12/10/2020", "12/9/2020", "12/8/2020", "12/7/2020", "12/6/2020", "12/5/2020", "12/4/2020", "12/3/2020", "12/2/2020", "12/1/2020", "11/30/2020", "11/29/2020", "149", "158", "161", "163", "170", "169", "181", "190", "195", "206", "208", "217", "232", "245", "252", "255", "260", "267", "304", "300", "297", "307", "303", "315", "326", "330", "339", "362", "387", "392", "407", "415", "433", "463", "491", "493", "511", "544", "571", "605", "610", "625", "613", "637", "658", "666", "691", "712", "728", "729", "742", "767", "786", "811", "817", "823", "836", "849", "866", "868", "886", "887", "869", "860", "877", "882", "899", "947", "950", "937", "906", "902", "913", "894", "903", "890", "896", "931", "918", "925", "885", "909", "924", "934", "954", "943", "923", "927", "953", "935", "955", "999", "1,011", "1,005", "1,012", "1,030", "1,043", "1,047", "1,076", "1,065", "1,083", "1,121", "1,132", "1,124", "1,154", "1,176", "1,148", "1,162", "1,199", "1,258", "1,273", "1,271", "1,270", "1,285", "1,328", "1,358", "1,402", "1,423", "1,412", "1,454", "1,459", "1,481", "1,516", "1,506", "1,522", "1,503", "1,500", "1,534", "1,551", "1,543", "1,584", "1,558", "1,544", "1,527", "1,562", "1,546", "1,560", "1,621", "1,614", "1,523", "1,550", "1,580", "1,570", "1,536", "1,501", "1,492", "1,426", "1,436", "1,428", "1,475", "1,424", "1,408", "1,392", "1,357", "1,344", "1,321", "1,292", "1,276", "1,250", "1,224", "1,222", "1,187", "1,129", "1,160", "1,166", "1,126", "1,095", "1,045", "1,088", "1,068", "1,098", "1,040", "1,009", "1,029", "1,007", "994", "952", "872", "850", "825", "795", "783", "718", "681", "%null%", "Null"]
								}, {
									"dataType": "datetime",
									"dataValues": ["2021-06-16 00:00:00", "2021-06-15 00:00:00", "2021-06-14 00:00:00", "2021-06-13 00:00:00", "2021-06-12 00:00:00", "2021-06-11 00:00:00", "2021-06-10 00:00:00", "2021-06-09 00:00:00", "2021-06-08 00:00:00", "2021-06-07 00:00:00", "2021-06-06 00:00:00", "2021-06-05 00:00:00", "2021-06-04 00:00:00", "2021-06-03 00:00:00", "2021-06-02 00:00:00", "2021-06-01 00:00:00", "2021-05-31 00:00:00", "2021-05-30 00:00:00", "2021-05-29 00:00:00", "2021-05-28 00:00:00", "2021-05-27 00:00:00", "2021-05-26 00:00:00", "2021-05-25 00:00:00", "2021-05-24 00:00:00", "2021-05-23 00:00:00", "2021-05-22 00:00:00", "2021-05-21 00:00:00", "2021-05-20 00:00:00", "2021-05-19 00:00:00", "2021-05-18 00:00:00", "2021-05-17 00:00:00", "2021-05-16 00:00:00", "2021-05-15 00:00:00", "2021-05-14 00:00:00", "2021-05-13 00:00:00", "2021-05-12 00:00:00", "2021-05-11 00:00:00", "2021-05-10 00:00:00", "2021-05-09 00:00:00", "2021-05-08 00:00:00", "2021-05-07 00:00:00", "2021-05-06 00:00:00", "2021-05-05 00:00:00", "2021-05-04 00:00:00", "2021-05-03 00:00:00", "2021-05-02 00:00:00", "2021-05-01 00:00:00", "2021-04-30 00:00:00", "2021-04-29 00:00:00", "2021-04-28 00:00:00", "2021-04-27 00:00:00", "2021-04-26 00:00:00", "2021-04-25 00:00:00", "2021-04-24 00:00:00", "2021-04-23 00:00:00", "2021-04-22 00:00:00", "2021-04-21 00:00:00", "2021-04-20 00:00:00", "2021-04-19 00:00:00", "2021-04-18 00:00:00", "2021-04-17 00:00:00", "2021-04-16 00:00:00", "2021-04-15 00:00:00", "2021-04-14 00:00:00", "2021-04-13 00:00:00", "2021-04-12 00:00:00", "2021-04-11 00:00:00", "2021-04-10 00:00:00", "2021-04-09 00:00:00", "2021-04-08 00:00:00", "2021-04-07 00:00:00", "2021-04-06 00:00:00", "2021-04-05 00:00:00", "2021-04-04 00:00:00", "2021-04-03 00:00:00", "2021-04-02 00:00:00", "2021-04-01 00:00:00", "2021-03-31 00:00:00", "2021-03-30 00:00:00", "2021-03-29 00:00:00", "2021-03-28 00:00:00", "2021-03-27 00:00:00", "2021-03-26 00:00:00", "2021-03-25 00:00:00", "2021-03-24 00:00:00", "2021-03-23 00:00:00", "2021-03-22 00:00:00", "2021-03-21 00:00:00", "2021-03-20 00:00:00", "2021-03-19 00:00:00", "2021-03-18 00:00:00", "2021-03-17 00:00:00", "2021-03-16 00:00:00", "2021-03-15 00:00:00", "2021-03-14 00:00:00", "2021-03-13 00:00:00", "2021-03-12 00:00:00", "2021-03-11 00:00:00", "2021-03-10 00:00:00", "2021-03-09 00:00:00", "2021-03-08 00:00:00", "2021-03-07 00:00:00", "2021-03-06 00:00:00", "2021-03-05 00:00:00", "2021-03-04 00:00:00", "2021-03-03 00:00:00", "2021-03-02 00:00:00", "2021-03-01 00:00:00", "2021-02-28 00:00:00", "2021-02-27 00:00:00", "2021-02-26 00:00:00", "2021-02-25 00:00:00", "2021-02-24 00:00:00", "2021-02-23 00:00:00", "2021-02-22 00:00:00", "2021-02-21 00:00:00", "2021-02-20 00:00:00", "2021-02-19 00:00:00", "2021-02-18 00:00:00", "2021-02-17 00:00:00", "2021-02-16 00:00:00", "2021-02-15 00:00:00", "2021-02-14 00:00:00", "2021-02-13 00:00:00", "2021-02-12 00:00:00", "2021-02-11 00:00:00", "2021-02-10 00:00:00", "2021-02-09 00:00:00", "2021-02-08 00:00:00", "2021-02-07 00:00:00", "2021-02-06 00:00:00", "2021-02-05 00:00:00", "2021-02-04 00:00:00", "2021-02-03 00:00:00", "2021-02-02 00:00:00", "2021-02-01 00:00:00", "2021-01-31 00:00:00", "2021-01-30 00:00:00", "2021-01-29 00:00:00", "2021-01-28 00:00:00", "2021-01-27 00:00:00", "2021-01-26 00:00:00", "2021-01-25 00:00:00", "2021-01-24 00:00:00", "2021-01-23 00:00:00", "2021-01-22 00:00:00", "2021-01-21 00:00:00", "2021-01-20 00:00:00", "2021-01-19 00:00:00", "2021-01-18 00:00:00", "2021-01-17 00:00:00", "2021-01-16 00:00:00", "2021-01-15 00:00:00", "2021-01-14 00:00:00", "2021-01-13 00:00:00", "2021-01-12 00:00:00", "2021-01-11 00:00:00", "2021-01-10 00:00:00", "2021-01-09 00:00:00", "2021-01-08 00:00:00", "2021-01-07 00:00:00", "2021-01-06 00:00:00", "2021-01-05 00:00:00", "2021-01-04 00:00:00", "2021-01-03 00:00:00", "2021-01-02 00:00:00", "2021-01-01 00:00:00", "2020-12-31 00:00:00", "2020-12-30 00:00:00", "2020-12-29 00:00:00", "2020-12-28 00:00:00", "2020-12-27 00:00:00", "2020-12-26 00:00:00", "2020-12-25 00:00:00", "2020-12-24 00:00:00", "2020-12-23 00:00:00", "2020-12-22 00:00:00", "2020-12-21 00:00:00", "2020-12-20 00:00:00", "2020-12-19 00:00:00", "2020-12-18 00:00:00", "2020-12-17 00:00:00", "2020-12-16 00:00:00", "2020-12-15 00:00:00", "2020-12-14 00:00:00", "2020-12-13 00:00:00", "2020-12-12 00:00:00", "2020-12-11 00:00:00", "2020-12-10 00:00:00", "2020-12-09 00:00:00", "2020-12-08 00:00:00", "2020-12-07 00:00:00", "2020-12-06 00:00:00", "2020-12-05 00:00:00", "2020-12-04 00:00:00", "2020-12-03 00:00:00", "2020-12-02 00:00:00", "2020-12-01 00:00:00", "2020-11-30 00:00:00", "2020-11-29 00:00:00"]
								}]
							}
						}
					},
					"underlyingDataTableColumns": [{
						"dataType": "cstring",
						"fieldCaption": "Measure Names",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[:Measure Names]",
						"isReferenced": true,
						"valueIndices": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						"formatValIdxs": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
						"aliasIndices": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
					}, {
						"dataType": "datetime",
						"fieldCaption": "RPT_DT",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[none:RPT_DT:ok]",
						"isReferenced": true,
						"valueIndices": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199],
						"formatValIdxs": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "real",
						"fieldCaption": "SUM(CURRENT_ICU_PATIENTS)",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[sum:CURRENT_ICU_PATIENTS:qk]",
						"isReferenced": true,
						"valueIndices": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 65, 71, 72, 73, 66, 74, 75, 64, 76, 72, 77, 78, 79, 80, 75, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 91, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 124, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 106, 163, 164, 165, 166, 167, 168, 169, 166, 170, 99, 171, 172, 173, 174, 175, 176, 70, 177, 178, 179, 180, 181, 50, 182, 183],
						"formatValIdxs": [202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 211, 212, 213, 214, 215, 216, 217, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 267, 273, 274, 275, 268, 276, 277, 266, 278, 274, 279, 280, 281, 282, 277, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 293, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 326, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 308, 365, 366, 367, 368, 369, 370, 371, 368, 372, 301, 373, 374, 375, 376, 377, 378, 272, 379, 380, 381, 382, 383, 252, 384, 385],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "real",
						"fieldCaption": "SUM(CURRENT_PATIENTS)",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[sum:CURRENT_PATIENTS:qk]",
						"isReferenced": true,
						"valueIndices": [-387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387, -387],
						"formatValIdxs": [387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387, 387],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}]
				}
			}
		}]
	}
}
"""

tableauDownloadableUnderlyingData = """
{
	"vqlCmdResponse": {
		"layoutStatus": {
		},
		"cmdResultList": [{
			"commandName": "tabdoc:get-underlying-data",
			"commandReturn": {
				"underlyingDataTable": {
					"tableAlias": "",
					"tableName": "",
					"numRows": 200,
					"dataDictionary": {
						"dataSegments": {
							"0": {
								"dataColumns": [{
									"dataType": "integer",
									"dataValues": [1]
								}, {
									"dataType": "real",
									"dataValues": [0, 6, 2, 1, 3, 5, 4, 10, 11, 7, 17, 9, 12, 8, 13, 14, 34, 26, 249, 128, 336, 20, 580, 568, 247, 32, 301, 48, 23, 18, 67, 449, 24, 148, 170, 593, 126, 37, 208, 471, 120, 49, 604, 348, 19, 246, 112, 311, 212, 371, 620, 163, 74, 381, 293, 252, 442, 286, 504, 714, 298, 1066, 43, 127, 149, 216, 136, 89, 322, 616, 863, 374, 217, 310, 288, 518, 452, 572, 200, 16, 625, 392, 483, 356, 40, 335, 287, 648, 419, 591, 965, 15, 73, 140, 626, 129, 90, 279, 105, 165, 215, 237, 354, 295, 60, 386, 264, 80, 30, 76, 69, 284, 188, 117, 268, 382, 275, 234, 109, 183, 195, 119, 46, 543, 52, 38, 41, 133, 45, 424, 54, 151, 359, 262, 401, 265, 337, 1457, 487, 334, 2142, 114, 223, 2341, 1426, 853, 197, 1171, 364, 130, 135, 116, 33, 1978, 407, 574, 28, 27, 155, 759, 2273, 1187, 797, 1273, 786, 319, 2580, 1288, 189, 922, 313, 214, 979, 173, 1870, 579, 50, 1490, 2003, 1095, 192, 831, 384, 2437, 544, 2334, 159, 1485, 70, 660, 2278, 4183, 1456, 3988, 31, 199, 62, 168, 908, 840, 1062, 655, 393, 1098, 2555, 4779, 1983, 495, 1193, 1538, 1216, 3452, 1465, 1797, 1997, 1310, 180, 71, 3545, 3834, 3764, 1135, 162, 1228, 1477, 3909, 2723, 1576, 994, 2671, 838, 4703, 206, 154, 3720, 213, 866, 2011, 912, 889, 982, 431, 1413, 1124, 56, 2108, 232, 1416, 1089, 598, 365, 528, 29, 485, 1687, 47, 2076, 1455, 556, 2217, 997, 1396, 1433, 643, 123, 829, 791, 441, 318, 113, 3254, 241, 2339, 160, 1533, 99, 94, 202, 665, 304, 957, 370, 3040, 97, 513, 1012, 1578, 1706, 2128, 432, 1077, 1563, 182]
								}, {
									"dataType": "cstring",
									"dataValues": ["Otsego", "Franklin", "Albany", "Chemung", "Cayuga", "New York", "Erie", "Westchester", "Orange", "Bronx", "Kings", "Chautauqua", "St. Lawrence", "Jefferson", "Sullivan", "Tompkins", "Chenango", "Ontario", "Schoharie", "Columbia", "Madison", "Steuben", "Onondaga", "Allegany", "Niagara", "Delaware", "Ulster", "Schenectady", "Queens", "Oneida", "Nassau", "Warren", "Suffolk", "Rockland", "Cortland", "Monroe", "Lewis", "Herkimer", "Orleans", "Dutchess", "Fulton", "Wayne", "Livingston", "Cattaraugus", "Oswego", "Broome", "Putnam", "Richmond", "Rensselaer", "Saratoga", "Schuyler", "Yates", "Montgomery", "Clinton", "Essex", "Genesee", "Wyoming", "Mohawk Valley", "North Country", "Capital Region", "Southern Tier", "Central New York", "New York City", "Western New York", "Mid-Hudson", "Finger Lakes", "Long Island", "42.457405", "44.343929", "42.65337", "42.099285", "42.940811", "40.739605", "42.508575", "41.076408", "41.367916", "40.843609", "40.655066", "40.689842", "42.480774", "42.900394", "44.676151", "43.986073", "41.709258", "41.74115", "42.469826", "42.541813", "44.692039", "42.960537", "44.162724", "42.68683", "42.246239", "42.814011", "40.58662", "42.141293", "43.041107", "42.213474", "43.026154", "42.165611", "43.176472", "41.732235", "42.819839", "40.74432", "42.92717", "42.875027", "43.098179", "40.755531", "42.875748", "40.871731", "43.30735", "40.696751", "41.112255", "44.338207", "42.609051", "40.81435", "41.92643", "41.213886", "43.135769", "40.765381", "40.879513", "40.67794", "42.372952", "40.857388", "40.701412", "40.757797", "42.900716", "40.93816", "42.977848", "40.655823", "40.659435", "40.737576", "40.773907", "43.795677", "40.817661", "43.043964", "40.778915", "40.728745", "40.753349", "40.681789", "%null%", "Null", "40.639423", "42.147694", "42.695793", "44.936363", "43.223637", "42.122921", "40.764386", "42.781742", "42.84853", "40.688408", "40.784775", "41.717392", "42.991219", "40.849575", "40.879951", "40.840431", "40.894569", "40.912476", "40.913021", "41.096249", "40.732666", "40.617954", "40.790482", "40.768269", "40.805912", "40.649601", "40.770092", "43.154659", "40.7503676", "40.8730537", "40.689615", "40.646591", "40.742874", "40.741699", "40.725353", "43.068096", "40.613419", "40.872475", "40.841415", "40.76408", "40.941673", "40.710426", "40.668087", "41.291512", "40.747517", "43.059728", "43.094048", "42.551964", "40.880512", "40.77924", "41.934223", "41.196774", "42.269238", "42.089844", "43.07869", "41.439953", "43.454781", "42.092606", "40.933643", "41.107639", "40.774471", "41.384766", "40.71722", "40.635807", "44.337296", "43.192619", "43.229935", "40.853909", "41.014721", "40.968262", "42.733574", "43.964928", "43.084843", "42.351536", "42.92905", "42.914642", "42.670712", "40.594237", "40.725014", "41.260586", "40.867531", "43.083561", "40.800301", "40.598637", "41.503017", "42.657539", "40.947533", "42.314438", "40.725853", "42.091446", "43.055744", "40.929512", "42.953758", "42.961201", "40.584141", "40.516773", "43.124336", "40.810238", "43.191551", "43.14901", "44.85677", "44.700279", "44.215466", "43.849476", "42.091236", "43.007816", "42.088062", "42.115063", "42.998436", "43.00404", "40.909217", "41.110958", "40.885757", "43.042622", "40.654518", "41.694523", "41.08773", "42.327965", "41.026333", "41.015186", "40.700535", "40.704517", "42.753513", "-75.053261", "-74.144363", "-73.773834", "-76.826782", "-76.564758", "-73.976509", "-78.659103", "-73.798767", "-74.682487", "-73.911545", "-73.912579", "-73.977455", "-79.33387", "-78.865707", "-74.981529", "-75.595421", "-74.737206", "-75.046593", "-76.536896", "-75.524773", "-75.499908", "-77.138863", "-75.055809", "-74.481976", "-73.776306", "-75.541962", "-73.965797", "-77.047562", "-76.137932", "-78.287506", "-78.862457", "-75.12812", "-78.670998", "-74.380661", "-73.918747", "-73.885719", "-78.829224", "-77.289818", "-75.275383", "-73.815475", "-76.987427", "-73.62159", "-73.645996", "-73.286324", "-74.133003", "-75.474411", "-76.186195", "-73.940506", "-73.995453", "-73.986", "-77.607544", "-73.954185", "-73.417442", "-73.937515", "-77.278656", "-73.846741", "-73.816299", "-74.0045151", "-78.867203", "-73.053894", "-78.878754", "-73.944099", "-73.934036", "-74.000488", "-73.960632", "-75.498146", "-73.92421", "-74.847458", "-72.978035", "-73.851036", "-73.706848", "-73.685814", "-73.99839", "-74.643089", "-74.922684", "-74.907951", "-78.397141", "-77.949974", "-73.956812", "-78.77224", "-78.812859", "-73.63324", "-73.94368", "-73.92942", "-78.72982", "-73.845055", "-73.880562", "-73.848244", "-73.86142", "-73.840004", "-73.787086", "-73.924957", "-73.981598", "-73.94323", "-73.953766", "-73.924461", "-73.961639", "-73.6315", "-73.987785", "-79.030556", "-73.8456118", "-73.9126905", "-73.997478", "-74.020439", "-73.974159", "-73.643082", "-73.554321", "-74.330643", "-73.948967", "-73.912773", "-73.940704", "-73.954926", "-73.836334", "-74.005486", "-73.978905", "-73.893341", "-73.826035", "-77.102244", "-79.0504", "-77.700195", "-73.881538", "-73.702888", "-73.912331", "-73.72451", "-74.91555", "-78.42688", "-75.654449", "-74.368744", "-76.516434", "-75.935646", "-72.674278", "-73.859665", "-73.478264", "-73.664413", "-73.803581", "-74.106674", "-75.919991", "-77.584503", "-75.443466", "-73.891014", "-73.862259", "-73.885033", "-73.671455", "-75.912827", "-73.796341", "-76.858627", "-78.849953", "-78.784241", "-77.059822", "-73.654958", "-73.240372", "-74.357185", "-73.220222", "-75.267189", "-73.669098", "-73.752769", "-74.015129", "-73.803879", "-73.060081", "-77.660164", "-73.478714", "-76.79686", "-76.149384", "-73.896957", "-74.216194", "-74.186272", "-74.086998", "-74.196808", "-77.623779", "-73.508614", "-77.701538", "-77.636139", "-74.291893", "-73.466751", "-73.596558", "-73.435593", "-79.232872", "-76.17025", "-75.91423", "-75.959122", "-78.181587", "-78.177475", "-73.115198", "-72.361282", "-72.380692", "-76.138809", "-73.945045", "-73.935799", "-73.803993", "-79.569412", "-73.769585", "-73.75573", "-73.941711", "-73.91774", "-78.132454", "A.O. Fox Memorial Hospital", "Adirondack Medical Center-Saranac Lake Site", "Albany Medical Center Hospital", "Arnot Ogden Medical Center", "Auburn Community Hospital", "Bellevue Hospital Center", "Bertrand Chaffee Hospital", "Blythedale Childrens Hospital", "Bon Secours Community Hospital", "BronxCare Hospital Center", "Brookdale Hospital Medical Center", "Brooklyn Hospital Center - Downtown Campus", "Brooks-TLC Hospital System, Inc.", "Buffalo General Medical Center", "Canton-Potsdam Hospital", "Carthage Area Hospital Inc", "Catskill Regional Medical Center", "Catskill Regional Medical Center - G. Hermann Site", "Cayuga Medical Center at Ithaca", "Chenango Memorial Hospital Inc", "Claxton-Hepburn Medical Center", "Clifton Springs Hospital and Clinic", "Clifton-Fine Hospital", "Cobleskill Regional Hospital", "Columbia Memorial Hospital", "Community Memorial Hospital Inc", "Coney Island Hospital", "Corning Hospital", "Crouse Hospital", "Cuba Memorial Hospital Inc", "Degraff Memorial Hospital", "Delaware Valley Hospital Inc", "Eastern Niagara Hospital - Lockport Division", "Ellenville Regional Hospital", "Ellis Hospital", "Elmhurst Hospital Center", "Erie County Medical Center", "F.F. Thompson Hospital", "Faxton-St Lukes Healthcare St Lukes Division", "Flushing Hospital Medical Center", "Geneva General Hospital", "Glen Cove Hospital", "Glens Falls Hospital", "Good Samaritan Hospital Medical Center", "Good Samaritan Hospital of Suffern", "Gouverneur Hospital", "Guthrie Cortland Medical Center", "Harlem Hospital Center", "HealthAlliance Hospital Broadway Campus", "Helen Hayes Hospital", "Highland Hospital", "Hospital for Special Surgery", "Huntington Hospital", "Interfaith Medical Center", "Ira Davenport Memorial Hospital", "Jacobi Medical Center", "Jamaica Hospital Medical Center", "Javits Center Hospital", "John R. Oishei Children's Hospital", "John T Mather Memorial Hospital of Port Jefferson New York Inc", "Kenmore Mercy Hospital", "Kings County Hospital Center", "Kingsbrook Jewish Medical Center", "Lenox Health Greenwich Village", "Lenox Hill Hospital", "Lewis County General Hospital", "Lincoln Medical and Mental Health Center", "Little Falls Hospital", "Long Island Community Hospital", "Long Island Jewish Forest Hills", "Long Island Jewish Medical Center", "Long Island Jewish Valley Stream", "Maimonides Crown Heights", "Maimonides Medical Center", "Margaretville Hospital", "Mary Imogene Bassett Hospital", "Massena Hospital, Inc.", "Medina Memorial Hospital", "Memorial Hosp of Wm F and Gertrude F Jones A/K/A Jones Memorial Hosp", "Memorial Hospital for Cancer and Allied Diseases", "Mercy Hospital - Mercy Hospital Orchard Park Division", "Mercy Hospital of Buffalo", "Mercy Medical Center", "Metropolitan Hospital Center", "Mid-Hudson Valley Division of Westchester Medical Center", "Millard Fillmore Suburban Hospital", "Montefiore Med Center - Jack D Weiler Hosp of A Einstein College Div", "Montefiore Medical Center - Henry and Lucy Moses Div", "Montefiore Medical Center - Montefiore Westchester Square", "Montefiore Medical Center-Wakefield Hospital", "Montefiore Mount Vernon Hospital", "Montefiore New Rochelle Hospital", "Montefiore Nyack", "Mount Sinai - Samaritans Purse", "Mount Sinai Beth Israel", "Mount Sinai Brooklyn", "Mount Sinai Hospital", "Mount Sinai Hospital - Mount Sinai Hospital of Queens", "Mount Sinai Morningside", "Mount Sinai South Nassau", "Mount Sinai West", "Mount St Marys Hospital and Health Center", "NYC H+H Billie Jean King Tennis Center", "NYC H+H Roosevelt Island Medical Center", "NYP - Ryan Larkin Field Hospital", "NYU Langone Health-Cobble Hill", "NYU Langone Hospital-Brooklyn", "NYU Langone Hospitals", "NYU Winthrop Hospital", "Nassau University Medical Center", "Nathan Littauer Hospital", "New York Community Hospital of Brooklyn, Inc", "New York-Presbyterian Hospital - Allen Hospital", "New York-Presbyterian Hospital - Columbia Presbyterian Center", "New York-Presbyterian Hospital - New York Weill Cornell Center", "New York-Presbyterian Lawrence Hospital", "New York-Presbyterian/Lower Manhattan Hospital", "NewYork-Presbyterian Brooklyn Methodist Hospital", "NewYork-Presbyterian/Hudson Valley Hospital", "NewYork-Presbyterian/Queens", "Newark-Wayne Community Hospital", "Niagara Falls Memorial Medical Center", "Nicholas H. Noyes Memorial Hospital", "North Central Bronx Hospital", "North Shore University Hospital", "Northern Dutchess Hospital", "Northern Westchester Hospital", "O'Connor Hospital", "Olean General Hospital", "Oneida Health Hospital", "Orange Regional Medical Center", "Oswego Hospital", "Our Lady of Lourdes Memorial Hospital Inc", "Peconic Bay Medical Center", "Phelps Hospital", "Plainview Hospital", "Putnam Hospital Center", "Queens Hospital Center", "Richmond University Medical Center", "River Hospital, Inc.", "Rochester General Hospital", "Rome Memorial Hospital, Inc", "SBH Health System", "SJRH - Dobbs Ferry Pavillion", "SJRH - St Johns Division", "Samaritan Hospital", "Samaritan Medical Center", "Saratoga Hospital", "Schuyler Hospital", "Sisters of Charity Hospital", "Sisters of Charity Hospital - St. Joseph Campus", "Soldiers and Sailors Memorial Hospital of Yates County Inc", "South Nassau Communities Hospital Off-Campus Emergency Department", "Southside Hospital", "St Anthony Community Hospital", "St Catherine of Siena Hospital", "St Elizabeth Medical Center", "St Francis Hospital", "St Johns Episcopal Hospital So Shore", "St Luke's Cornwall Hospital/Newburgh", "St Peters Hospital", "St. Charles Hospital", "St. James Hospital", "St. Joseph Hospital", "St. Joseph's Hospital", "St. Joseph's Hospital Health Center", "St. Joseph's Medical Center", "St. Mary's Healthcare", "St. Mary's Healthcare - Amsterdam Memorial Campus", "Staten Island University Hosp-North", "Staten Island University Hosp-South", "Strong Memorial Hospital", "Syosset Hospital", "The Unity Hospital of Rochester", "The Unity Hospital of Rochester - St. Mary's Campus", "The University of Vermont Health Network - Alice Hyde Medical Center", "The University of Vermont Health Network - Champlain Valley Physicians Hospital", "The University of Vermont Health Network - Elizabethtown Community Hospital", "The University of Vermont Health Network-Elizabethtown Community Hospital Moses Ludington", "UPMC Chautauqua at WCA", "UPSTATE University Hospital at Community General", "United Health Services Hospitals Inc. - Binghamton General Hospital", "United Health Services Hospitals Inc. - Wilson Medical Center", "United Memorial Medical Center Bank Street Campus", "United Memorial Medical Center North Street Campus", "University Hospital", "University Hospital - Stony Brook Eastern Long Island Hospital", "University Hospital - Stony Brook Southampton Hospital", "University Hospital SUNY Health Science Center", "University Hospital of Brooklyn", "Vassar Brothers Medical Center", "Westchester Medical Center", "Westfield Memorial Hospital Inc", "White Plains Hospital Center", "Winifred Masterson Burke Rehabilitation Hospital", "Woodhull Medical and Mental Health Center", "Wyckoff Heights Medical Center", "Wyoming County Community Hospital", "Bassett Healthcare Network", "Independent", "Albany Medical Center", "Arnot Health", "NYC H+H", "Westchester Medical Center Health Network", "One Brooklyn Health System", "Kaleida Health", "St. Lawrence Health System", "Garnet Health -formerly Greater Hudson Valley Health System", "Cayuga Health System", "United Health Services Hospitals, Inc.", "North Star Health Alliance", "Rochester Regional Health System ", "Crouse Health", "The Guthrie Clinic", "University of Rochester Medical Center", "Mohawk Valley Health System", "MediSys Health Network", "Finger Lakes Health", "Northwell Health", "Catholic Health Services of Long Island", "New York-Presbyterian Healthcare System", "Catholic Health, Buffalo", "Montefiore Healthcare System", "Mount Sinai Health System", "NYU Langone Health", "Nuvance Health", "Ascension Health", "St. Josephs Hospital Syracuse NY", "Riverside Health Care System, Inc.", "St. Peters Health Partners", "Trinity", "University of Vermont Health Network", "The University of Vermont Health Network", "The University of Vermont Health Network Elizabeth", "UPMC", "Stony Brook Medicine", "Allegheny Health Network", "NYC Voluntary", "Capital District Regional Office", "Western Regional Office ", "Central New York Regional Office", "Metropolitan Area Regional Office ", "False", "True", "6/16/2021", "6/15/2021", "Rest of State", "NYC", "0", "6", "2", "1", "3", "5", "4", "10", "0.00000", "3.00000", "2.00000", "1.00000", "5.00000", "6.00000", "11", "7", "17", "9", "12", "8", "13", "14", "34", "26", "6/17/2021", "12.00", "1.00", "249.00", "128.00", "26.00", "336.00", "9.00", "0.00", "20.00", "580.00", "568.00", "247.00", "32.00", "301.00", "8.00", "48.00", "23.00", "18.00", "10.00", "4.00", "67.00", "13.00", "449.00", "24.00", "148.00", "2.00", "170.00", "593.00", "126.00", "37.00", "208.00", "471.00", "120.00", "49.00", "604.00", "348.00", "19.00", "246.00", "112.00", "311.00", "212.00", "3.00", "371.00", "620.00", "163.00", "74.00", "381.00", "293.00", "252.00", "11.00", "442.00", "6.00", "286.00", "504.00", "714.00", "298.00", "1,066.00", "43.00", "127.00", "149.00", "216.00", "136.00", "89.00", "322.00", "616.00", "863.00", "374.00", "217.00", "310.00", "288.00", "518.00", "452.00", "572.00", "200.00", "16.00", "625.00", "392.00", "483.00", "356.00", "40.00", "335.00", "287.00", "648.00", "419.00", "591.00", "965.00", "15.00", "73.00", "140.00", "626.00", "129.00", "90.00", "279.00", "105.00", "165.00", "215.00", "237.00", "354.00", "295.00", "60.00", "386.00", "264.00", "80.00", "30.00", "76.00", "69.00", "284.00", "5.00", "188.00", "117.00", "268.00", "382.00", "275.00", "234.00", "109.00", "183.00", "195.00", "119.00", "46.00", "543.00", "52.00", "38.00", "41.00", "133.00", "45.00", "424.00", "54.00", "151.00", "359.00", "262.00", "401.00", "265.00", "337.00", "17.00", "1,457.00", "487.00", "334.00", "2,142.00", "114.00", "223.00", "2,341.00", "1,426.00", "853.00", "197.00", "1,171.00", "364.00", "130.00", "135.00", "116.00", "33.00", "1,978.00", "407.00", "574.00", "28.00", "27.00", "155.00", "759.00", "2,273.00", "1,187.00", "797.00", "1,273.00", "786.00", "319.00", "2,580.00", "1,288.00", "189.00", "922.00", "313.00", "214.00", "979.00", "173.00", "1,870.00", "579.00", "50.00", "1,490.00", "2,003.00", "1,095.00", "192.00", "831.00", "384.00", "2,437.00", "544.00", "2,334.00", "159.00", "1,485.00", "70.00", "660.00", "2,278.00", "4,183.00", "1,456.00", "3,988.00", "31.00", "199.00", "62.00", "168.00", "908.00", "7.00", "840.00", "1,062.00", "655.00", "393.00", "1,098.00", "2,555.00", "4,779.00", "1,983.00", "495.00", "1,193.00", "1,538.00", "1,216.00", "3,452.00", "1,465.00", "1,797.00", "1,997.00", "1,310.00", "180.00", "71.00", "3,545.00", "3,834.00", "3,764.00", "1,135.00", "162.00", "1,228.00", "1,477.00", "3,909.00", "2,723.00", "1,576.00", "994.00", "2,671.00", "838.00", "4,703.00", "206.00", "154.00", "3,720.00", "213.00", "866.00", "2,011.00", "912.00", "889.00", "982.00", "431.00", "1,413.00", "1,124.00", "56.00", "2,108.00", "232.00", "1,416.00", "1,089.00", "598.00", "365.00", "528.00", "29.00", "485.00", "1,687.00", "47.00", "2,076.00", "1,455.00", "556.00", "2,217.00", "997.00", "1,396.00", "1,433.00", "643.00", "123.00", "829.00", "791.00", "441.00", "318.00", "113.00", "3,254.00", "241.00", "2,339.00", "160.00", "1,533.00", "99.00", "94.00", "202.00", "665.00", "304.00", "957.00", "370.00", "3,040.00", "97.00", "513.00", "1,012.00", "1,578.00", "1,706.00", "2,128.00", "432.00", "1,077.00", "1,563.00", "182.00"]
								}, {
									"dataType": "datetime",
									"dataValues": ["2021-06-16 00:00:00", "2021-06-15 00:00:00"]
								}, {
									"dataType": "boolean",
									"dataValues": [false, true]
								}, {
									"dataType": "date",
									"dataValues": ["2021-06-17", "2021-06-16"]
								}]
							}
						}
					},
					"underlyingDataTableColumns": [{
						"dataType": "cstring",
						"fieldCaption": "COUNTY",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[COUNTY]",
						"valueIndices": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 6, 12, 13, 14, 14, 15, 16, 12, 17, 12, 18, 19, 20, 10, 21, 22, 23, 24, 25, 24, 26, 27, 28, 6, 17, 29, 28, 17, 30, 31, 32, 33, 12, 34, 5, 26, 33, 35, 5, 32, 10, 21, 9, 28, 5, 6, 32, 6, 10, 10, 5, 5, 36, 9, 37, 32, 28, 28, 30, 10, 10, 25, 0, 12, 38, 23, 5, 6, 6, 30, 5, 39, 6, 9, 9, 9, 9, 7, 7, 33, 5, 5, 10, 5, 28, 5, 30, 5, 24, 28, 5, 5, 10, 10, 5, 30, 30, 40, 10, 5, 5, 5, 7, 5, 10, 7, 28, 41, 24, 42, 9, 30, 39, 7, 25, 43, 20, 8, 44, 45, 32, 7, 30, 46, 28, 47, 13, 35, 29, 9, 7, 7, 48, 13, 49, 50, 6, 6, 51, 30, 32, 8, 32, 29, 30, 28, 8, 2, 32, 21, 30, 3, 22, 7, 52, 52, 47, 47, 35, 30, 35, 35, 1, 53, 54, 54, 11, 22, 45, 45, 55, 55, 32, 32, 32, 22, 10, 39, 7, 11, 7, 7, 10, 10, 56, 0, 1],
						"formatValIdxs": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 6, 12, 13, 14, 14, 15, 16, 12, 17, 12, 18, 19, 20, 10, 21, 22, 23, 24, 25, 24, 26, 27, 28, 6, 17, 29, 28, 17, 30, 31, 32, 33, 12, 34, 5, 26, 33, 35, 5, 32, 10, 21, 9, 28, 5, 6, 32, 6, 10, 10, 5, 5, 36, 9, 37, 32, 28, 28, 30, 10, 10, 25, 0, 12, 38, 23, 5, 6, 6, 30, 5, 39, 6, 9, 9, 9, 9, 7, 7, 33, 5, 5, 10, 5, 28, 5, 30, 5, 24, 28, 5, 5, 10, 10, 5, 30, 30, 40, 10, 5, 5, 5, 7, 5, 10, 7, 28, 41, 24, 42, 9, 30, 39, 7, 25, 43, 20, 8, 44, 45, 32, 7, 30, 46, 28, 47, 13, 35, 29, 9, 7, 7, 48, 13, 49, 50, 6, 6, 51, 30, 32, 8, 32, 29, 30, 28, 8, 2, 32, 21, 30, 3, 22, 7, 52, 52, 47, 47, 35, 30, 35, 35, 1, 53, 54, 54, 11, 22, 45, 45, 55, 55, 32, 32, 32, 22, 10, 39, 7, 11, 7, 7, 10, 10, 56, 0, 1],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "cstring",
						"fieldCaption": "ECON_REGION",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[ECON_REGION]",
						"isReferenced": true,
						"valueIndices": [57, 58, 59, 60, 61, 62, 63, 64, 64, 62, 62, 62, 63, 63, 58, 58, 64, 64, 60, 60, 58, 65, 58, 57, 59, 61, 62, 60, 61, 63, 63, 60, 63, 64, 59, 62, 63, 65, 57, 62, 65, 66, 59, 66, 64, 58, 61, 62, 64, 64, 65, 62, 66, 62, 60, 62, 62, 62, 63, 66, 63, 62, 62, 62, 62, 58, 62, 57, 66, 62, 62, 66, 62, 62, 60, 57, 58, 65, 63, 62, 63, 63, 66, 62, 64, 63, 62, 62, 62, 62, 64, 64, 64, 62, 62, 62, 62, 62, 62, 66, 62, 63, 62, 62, 62, 62, 62, 62, 66, 66, 57, 62, 62, 62, 62, 64, 62, 62, 64, 62, 65, 63, 65, 62, 66, 64, 64, 60, 63, 61, 64, 61, 60, 66, 64, 66, 64, 62, 62, 58, 65, 57, 62, 64, 64, 59, 58, 59, 60, 63, 63, 65, 66, 66, 64, 66, 57, 66, 62, 64, 59, 66, 60, 66, 60, 61, 64, 57, 57, 62, 62, 65, 66, 65, 65, 58, 58, 58, 58, 63, 61, 60, 60, 65, 65, 66, 66, 66, 61, 62, 64, 64, 63, 64, 64, 62, 62, 65, 57, 58],
						"formatValIdxs": [57, 58, 59, 60, 61, 62, 63, 64, 64, 62, 62, 62, 63, 63, 58, 58, 64, 64, 60, 60, 58, 65, 58, 57, 59, 61, 62, 60, 61, 63, 63, 60, 63, 64, 59, 62, 63, 65, 57, 62, 65, 66, 59, 66, 64, 58, 61, 62, 64, 64, 65, 62, 66, 62, 60, 62, 62, 62, 63, 66, 63, 62, 62, 62, 62, 58, 62, 57, 66, 62, 62, 66, 62, 62, 60, 57, 58, 65, 63, 62, 63, 63, 66, 62, 64, 63, 62, 62, 62, 62, 64, 64, 64, 62, 62, 62, 62, 62, 62, 66, 62, 63, 62, 62, 62, 62, 62, 62, 66, 66, 57, 62, 62, 62, 62, 64, 62, 62, 64, 62, 65, 63, 65, 62, 66, 64, 64, 60, 63, 61, 64, 61, 60, 66, 64, 66, 64, 62, 62, 58, 65, 57, 62, 64, 64, 59, 58, 59, 60, 63, 63, 65, 66, 66, 64, 66, 57, 66, 62, 64, 59, 66, 60, 66, 60, 61, 64, 57, 57, 62, 62, 65, 66, 65, 65, 58, 58, 58, 58, 63, 61, 60, 60, 65, 65, 66, 66, 66, 61, 62, 64, 64, 63, 64, 64, 62, 62, 65, 57, 58],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "cstring",
						"fieldCaption": "FAC_LAT",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[FAC_LAT]",
						"valueIndices": [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 139, 161, 162, 163, 164, 165, 166, 167, 168, 169, 139, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 67, 68],
						"formatValIdxs": [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 140, 161, 162, 163, 164, 165, 166, 167, 168, 169, 140, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 67, 68],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "cstring",
						"fieldCaption": "FAC_LONG",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[FAC_LONG]",
						"valueIndices": [264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 139, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 139, 356, 357, 358, 359, 360, 361, 362, 363, 364, 139, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 264, 265],
						"formatValIdxs": [264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 140, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 140, 356, 357, 358, 359, 360, 361, 362, 363, 364, 140, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 264, 265],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "cstring",
						"fieldCaption": "HOSPITAL",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[HOSPITAL]",
						"valueIndices": [459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 459, 460],
						"formatValIdxs": [459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 459, 460],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "cstring",
						"fieldCaption": "HOSPITAL_NETWORK",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[HOSPITAL_NETWORK]",
						"valueIndices": [657, 658, 659, 660, 658, 661, 658, 658, 662, 658, 663, 658, 658, 664, 665, 658, 666, 666, 667, 668, 669, 670, 658, 657, 659, 671, 661, 672, 671, 658, 664, 668, 658, 658, 658, 661, 658, 673, 674, 675, 676, 677, 658, 678, 662, 665, 672, 661, 662, 679, 673, 658, 677, 663, 660, 661, 675, 658, 664, 677, 680, 661, 663, 677, 677, 658, 661, 657, 658, 677, 677, 677, 658, 658, 662, 657, 665, 658, 673, 658, 680, 680, 678, 661, 662, 664, 681, 681, 681, 681, 681, 681, 681, 658, 682, 682, 682, 682, 682, 682, 682, 680, 658, 658, 658, 683, 683, 683, 683, 658, 658, 658, 679, 679, 679, 679, 679, 679, 679, 679, 670, 658, 673, 661, 677, 684, 677, 657, 664, 658, 666, 658, 685, 677, 677, 677, 684, 661, 658, 658, 670, 686, 658, 687, 687, 688, 658, 659, 667, 680, 680, 676, 682, 677, 662, 678, 674, 678, 658, 681, 688, 678, 673, 678, 660, 689, 658, 685, 685, 677, 677, 673, 677, 670, 670, 690, 690, 691, 692, 693, 658, 668, 668, 670, 670, 694, 694, 694, 658, 658, 684, 662, 695, 681, 681, 661, 658, 658, 657, 658],
						"formatValIdxs": [657, 658, 659, 660, 658, 661, 658, 658, 662, 658, 663, 658, 658, 664, 665, 658, 666, 666, 667, 668, 669, 670, 658, 657, 659, 671, 661, 672, 671, 658, 664, 668, 658, 658, 658, 661, 658, 673, 674, 675, 676, 677, 658, 678, 662, 665, 672, 661, 662, 679, 673, 658, 677, 663, 660, 661, 675, 658, 664, 677, 680, 661, 663, 677, 677, 658, 661, 657, 658, 677, 677, 677, 658, 658, 662, 657, 665, 658, 673, 658, 680, 680, 678, 661, 662, 664, 681, 681, 681, 681, 681, 681, 681, 658, 682, 682, 682, 682, 682, 682, 682, 680, 658, 658, 658, 683, 683, 683, 683, 658, 658, 658, 679, 679, 679, 679, 679, 679, 679, 679, 670, 658, 673, 661, 677, 684, 677, 657, 664, 658, 666, 658, 685, 677, 677, 677, 684, 661, 658, 658, 670, 686, 658, 687, 687, 688, 658, 659, 667, 680, 680, 676, 682, 677, 662, 678, 674, 678, 658, 681, 688, 678, 673, 678, 660, 689, 658, 685, 685, 677, 677, 673, 677, 670, 670, 690, 690, 691, 692, 693, 658, 668, 668, 670, 670, 694, 694, 694, 658, 658, 684, 662, 695, 681, 681, 661, 658, 658, 657, 658],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "cstring",
						"fieldCaption": "NYC_IND",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[NYC_IND]",
						"valueIndices": [139, 139, 139, 139, 139, 661, 139, 139, 139, 696, 696, 696, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 661, 139, 139, 139, 139, 139, 139, 139, 139, 661, 139, 139, 139, 696, 139, 139, 139, 139, 139, 139, 139, 661, 139, 139, 139, 696, 139, 696, 139, 661, 696, 696, 139, 139, 139, 661, 696, 696, 696, 139, 661, 139, 139, 696, 696, 139, 696, 696, 139, 139, 139, 139, 139, 696, 139, 139, 139, 661, 139, 139, 696, 696, 696, 696, 139, 139, 139, 696, 696, 696, 696, 696, 696, 139, 696, 139, 696, 696, 696, 696, 696, 696, 139, 139, 139, 696, 696, 696, 696, 139, 696, 696, 139, 696, 139, 139, 139, 661, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 661, 696, 139, 139, 139, 696, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 696, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 696, 696, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 139, 696, 139, 139, 139, 139, 139, 661, 696, 139, 139, 139],
						"formatValIdxs": [140, 140, 140, 140, 140, 661, 140, 140, 140, 696, 696, 696, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 661, 140, 140, 140, 140, 140, 140, 140, 140, 661, 140, 140, 140, 696, 140, 140, 140, 140, 140, 140, 140, 661, 140, 140, 140, 696, 140, 696, 140, 661, 696, 696, 140, 140, 140, 661, 696, 696, 696, 140, 661, 140, 140, 696, 696, 140, 696, 696, 140, 140, 140, 140, 140, 696, 140, 140, 140, 661, 140, 140, 696, 696, 696, 696, 140, 140, 140, 696, 696, 696, 696, 696, 696, 140, 696, 140, 696, 696, 696, 696, 696, 696, 140, 140, 140, 696, 696, 696, 696, 140, 696, 696, 140, 696, 140, 140, 140, 661, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 661, 696, 140, 140, 140, 696, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 696, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 696, 696, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 696, 140, 140, 140, 140, 140, 661, 696, 140, 140, 140],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "cstring",
						"fieldCaption": "REGION",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[REGION]",
						"valueIndices": [697, 697, 697, 698, 699, 700, 698, 700, 700, 700, 700, 700, 698, 698, 699, 699, 700, 700, 699, 699, 699, 698, 699, 697, 697, 699, 700, 698, 699, 698, 698, 697, 698, 700, 697, 700, 698, 698, 699, 700, 698, 700, 697, 700, 700, 699, 699, 700, 700, 700, 698, 700, 700, 700, 698, 700, 700, 700, 698, 700, 698, 700, 700, 700, 700, 699, 700, 699, 700, 700, 700, 700, 700, 700, 697, 697, 699, 698, 698, 700, 698, 698, 700, 700, 700, 698, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 698, 700, 700, 700, 700, 700, 700, 700, 700, 697, 700, 700, 700, 700, 700, 700, 700, 700, 700, 698, 698, 698, 700, 700, 700, 700, 697, 698, 699, 700, 699, 699, 700, 700, 700, 700, 700, 700, 699, 698, 699, 700, 700, 700, 697, 699, 697, 698, 698, 698, 698, 700, 700, 700, 700, 699, 700, 700, 700, 697, 700, 698, 700, 698, 699, 700, 697, 697, 700, 700, 698, 700, 698, 698, 697, 697, 697, 697, 698, 699, 699, 699, 698, 698, 700, 700, 700, 699, 700, 700, 700, 698, 700, 700, 700, 700, 698, 697, 697],
						"formatValIdxs": [697, 697, 697, 698, 699, 700, 698, 700, 700, 700, 700, 700, 698, 698, 699, 699, 700, 700, 699, 699, 699, 698, 699, 697, 697, 699, 700, 698, 699, 698, 698, 697, 698, 700, 697, 700, 698, 698, 699, 700, 698, 700, 697, 700, 700, 699, 699, 700, 700, 700, 698, 700, 700, 700, 698, 700, 700, 700, 698, 700, 698, 700, 700, 700, 700, 699, 700, 699, 700, 700, 700, 700, 700, 700, 697, 697, 699, 698, 698, 700, 698, 698, 700, 700, 700, 698, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 698, 700, 700, 700, 700, 700, 700, 700, 700, 697, 700, 700, 700, 700, 700, 700, 700, 700, 700, 698, 698, 698, 700, 700, 700, 700, 697, 698, 699, 700, 699, 699, 700, 700, 700, 700, 700, 700, 699, 698, 699, 700, 700, 700, 697, 699, 697, 698, 698, 698, 698, 700, 700, 700, 700, 699, 700, 700, 700, 697, 700, 698, 700, 698, 699, 700, 697, 697, 700, 700, 698, 700, 698, 698, 697, 697, 697, 697, 698, 699, 699, 699, 698, 698, 700, 700, 700, 699, 700, 700, 700, 698, 700, 700, 700, 700, 698, 697, 697],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "boolean",
						"fieldCaption": "RegionFilter",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[Calculation_1832402148469100546]",
						"valueIndices": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						"formatValIdxs": [701, 701, 702, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 702, 701, 701, 701, 701, 701, 701, 701, 701, 701, 702, 701, 701, 701, 701, 701, 701, 701, 702, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 702, 701, 702, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 702, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "datetime",
						"fieldCaption": "RPT_DT",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[RPT_DT]",
						"isReferenced": true,
						"valueIndices": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
						"formatValIdxs": [703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 703, 704, 704],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "cstring",
						"fieldCaption": "SUB_REGION",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[SUB_REGION]",
						"valueIndices": [705, 705, 705, 705, 705, 706, 705, 7, 705, 706, 706, 706, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 706, 705, 705, 705, 705, 705, 705, 705, 705, 706, 705, 705, 705, 706, 705, 66, 705, 66, 705, 705, 705, 706, 705, 705, 705, 706, 66, 706, 705, 706, 706, 706, 705, 66, 705, 706, 706, 706, 706, 705, 706, 705, 66, 706, 706, 66, 706, 706, 705, 705, 705, 705, 705, 706, 705, 705, 66, 706, 705, 705, 706, 706, 706, 706, 7, 7, 705, 706, 706, 706, 706, 706, 706, 66, 706, 705, 706, 706, 706, 706, 706, 706, 66, 66, 705, 706, 706, 706, 706, 7, 706, 706, 7, 706, 705, 705, 705, 706, 66, 705, 7, 705, 705, 705, 705, 705, 705, 66, 7, 66, 705, 706, 706, 705, 705, 705, 706, 7, 7, 705, 705, 705, 705, 705, 705, 705, 66, 66, 705, 66, 705, 66, 706, 705, 705, 66, 705, 66, 705, 705, 7, 705, 705, 706, 706, 705, 66, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 66, 66, 66, 705, 706, 705, 7, 705, 7, 7, 706, 706, 705, 705, 705],
						"formatValIdxs": [705, 705, 705, 705, 705, 706, 705, 7, 705, 706, 706, 706, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 706, 705, 705, 705, 705, 705, 705, 705, 705, 706, 705, 705, 705, 706, 705, 66, 705, 66, 705, 705, 705, 706, 705, 705, 705, 706, 66, 706, 705, 706, 706, 706, 705, 66, 705, 706, 706, 706, 706, 705, 706, 705, 66, 706, 706, 66, 706, 706, 705, 705, 705, 705, 705, 706, 705, 705, 66, 706, 705, 705, 706, 706, 706, 706, 7, 7, 705, 706, 706, 706, 706, 706, 706, 66, 706, 705, 706, 706, 706, 706, 706, 706, 66, 66, 705, 706, 706, 706, 706, 7, 706, 706, 7, 706, 705, 705, 705, 706, 66, 705, 7, 705, 705, 705, 705, 705, 705, 66, 7, 66, 705, 706, 706, 705, 705, 705, 706, 7, 7, 705, 705, 705, 705, 705, 705, 705, 66, 66, 705, 66, 705, 66, 706, 705, 705, 66, 705, 66, 705, 705, 7, 705, 705, 706, 706, 705, 66, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 705, 66, 66, 66, 705, 706, 705, 7, 705, 7, 7, 706, 706, 705, 705, 705],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "real",
						"fieldCaption": "CURRENT_ICU_PATIENTS",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[CURRENT_ICU_PATIENTS]",
						"isReferenced": true,
						"valueIndices": [0, 0, 1, 2, 3, 4, 0, 0, 0, 3, 0, 2, 0, 2, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 5, 3, 0, 0, 0, 0, 3, 0, 2, 0, 3, 0, 0, 0, 2, 0, 3, 2, 0, 0, 0, -140, 0, 0, 2, 0, 0, 0, 0, 0, 4, 0, 3, 2, 3, 3, -140, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3, 0, 0, 0, 3, 3, -140, 3, 2, 2, 3, 0, 0, 2, 3, -140, -140, -140, 0, 3, 4, 3, 0, 0, 0, 3, 6, 6, 0, 0, 2, 3, 0, 0, 0, 0, 2, 2, 0, 3, 0, 2, 0, 0, 3, 0, 0, 3, 0, 0, 0, 2, 0, 2, 2, 1, 0, 0, 0, 3, 3, 0, 3, 0, 0, 0, 3, 0, 2, 3, 4, 0, 3, 3, 3, 0, 3, 0, 3, 0, 0, 0, 5, 0, 7, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 0, 6, 3, 0, 2, 0, 0, 0, 3, 3, 0, 0, 0],
						"formatValIdxs": [707, 707, 708, 709, 710, 711, 707, 707, 707, 710, 707, 709, 707, 709, 710, 707, 707, 707, 710, 707, 707, 707, 707, 707, 707, 707, 709, 707, 709, 707, 707, 707, 707, 707, 707, 707, 712, 710, 707, 707, 707, 707, 710, 707, 709, 707, 710, 707, 707, 707, 709, 707, 710, 709, 707, 707, 707, 140, 707, 707, 709, 707, 707, 707, 707, 707, 711, 707, 710, 709, 710, 710, 140, 707, 707, 707, 707, 707, 707, 707, 707, 707, 707, 707, 707, 710, 711, 710, 707, 707, 707, 710, 710, 140, 710, 709, 709, 710, 707, 707, 709, 710, 140, 140, 140, 707, 710, 711, 710, 707, 707, 707, 710, 713, 713, 707, 707, 709, 710, 707, 707, 707, 707, 709, 709, 707, 710, 707, 709, 707, 707, 710, 707, 707, 710, 707, 707, 707, 709, 707, 709, 709, 708, 707, 707, 707, 710, 710, 707, 710, 707, 707, 707, 710, 707, 709, 710, 711, 707, 710, 710, 710, 707, 710, 707, 710, 707, 707, 707, 712, 707, 714, 707, 710, 707, 707, 707, 707, 707, 707, 707, 707, 710, 707, 707, 708, 707, 707, 713, 710, 707, 709, 707, 707, 707, 710, 710, 707, 707, 707],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "real",
						"fieldCaption": "CURRENT_INTUBATED_PATIENTS",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[CURRENT_INTUBATED_PATIENTS]",
						"valueIndices": [0, 0, 4, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 3, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, -140, 0, 0, 2, 0, 0, 0, 0, 0, 4, 0, 3, 3, 3, 3, -140, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 3, 0, 0, 0, 3, 3, -140, 3, 3, 0, 3, 0, 0, 2, 3, -140, -140, -140, 0, 3, 2, 3, 0, 0, 0, 0, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 3, 4, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 3, 0, 3, 0, 0, 0, 3, 3, 0, 0, 0],
						"formatValIdxs": [715, 715, 716, 715, 715, 717, 715, 715, 715, 715, 715, 718, 715, 718, 718, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 718, 715, 715, 715, 715, 715, 715, 715, 715, 715, 719, 718, 715, 715, 715, 715, 715, 715, 717, 715, 715, 715, 715, 715, 718, 715, 715, 718, 715, 715, 715, 140, 715, 715, 717, 715, 715, 715, 715, 715, 716, 715, 718, 718, 718, 718, 140, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 718, 717, 718, 715, 715, 715, 718, 718, 140, 718, 718, 715, 718, 715, 715, 717, 718, 140, 140, 140, 715, 718, 717, 718, 715, 715, 715, 715, 716, 717, 715, 715, 715, 715, 715, 715, 715, 715, 718, 717, 715, 715, 715, 717, 715, 715, 715, 715, 715, 715, 715, 715, 715, 718, 715, 718, 718, 716, 715, 715, 715, 715, 715, 715, 718, 715, 715, 715, 718, 715, 715, 718, 715, 715, 718, 715, 718, 715, 715, 715, 715, 715, 715, 715, 717, 715, 720, 715, 718, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 720, 715, 715, 717, 718, 715, 718, 715, 715, 715, 718, 718, 715, 715, 715],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "real",
						"fieldCaption": "CURRENT_PATIENTS",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[CURRENT_PATIENTS]",
						"isReferenced": true,
						"valueIndices": [0, 0, 8, 5, 2, 6, 0, 0, 0, 2, 8, 4, 3, 6, 6, 0, 2, 0, 4, 0, 0, 0, 0, 0, 2, 3, 1, 2, 9, 2, 0, 3, 0, 0, 5, 3, 10, 2, 3, 6, 3, 0, 4, 11, 4, 0, 6, 6, 0, 0, 12, 0, 3, 2, 0, 3, 1, -140, 3, 5, 2, 13, 0, 0, 2, 0, 1, 3, 9, 9, 7, 4, -140, 14, 3, 4, 0, 3, 0, 3, 0, 2, 6, 2, 2, 3, 6, 9, 0, 2, 0, 2, 2, -140, 3, 4, 9, 5, 4, 0, 1, 3, -140, -140, -140, 0, 4, 7, 1, 4, 0, 6, 2, 10, 14, 2, 4, 14, 2, 7, 0, 3, 0, 5, 1, 0, 3, 0, 2, 3, 11, 2, 3, 0, 3, 0, 0, 2, 4, 0, 14, 2, 1, 0, 2, 0, 2, 4, 0, 1, 0, 0, 0, 3, 0, 4, 3, 4, 3, 5, 1, 4, 0, 4, 0, 4, 0, 0, 0, 15, 0, 16, 0, 4, 0, 0, 6, 0, 0, 3, 2, 3, 7, 0, 0, 17, 0, 0, 9, 2, 2, 5, 0, 4, 3, 4, 4, 0, 0, 0],
						"formatValIdxs": [707, 707, 721, 712, 709, 713, 707, 707, 707, 709, 721, 711, 710, 713, 713, 707, 709, 707, 711, 707, 707, 707, 707, 707, 709, 710, 708, 709, 722, 709, 707, 710, 707, 707, 712, 710, 723, 709, 710, 713, 710, 707, 711, 724, 711, 707, 713, 713, 707, 707, 725, 707, 710, 709, 707, 710, 708, 140, 710, 712, 709, 726, 707, 707, 709, 707, 708, 710, 722, 722, 714, 711, 140, 727, 710, 711, 707, 710, 707, 710, 707, 709, 713, 709, 709, 710, 713, 722, 707, 709, 707, 709, 709, 140, 710, 711, 722, 712, 711, 707, 708, 710, 140, 140, 140, 707, 711, 714, 708, 711, 707, 713, 709, 723, 727, 709, 711, 727, 709, 714, 707, 710, 707, 712, 708, 707, 710, 707, 709, 710, 724, 709, 710, 707, 710, 707, 707, 709, 711, 707, 727, 709, 708, 707, 709, 707, 709, 711, 707, 708, 707, 707, 707, 710, 707, 711, 710, 711, 710, 712, 708, 711, 707, 711, 707, 711, 707, 707, 707, 728, 707, 729, 707, 711, 707, 707, 713, 707, 707, 710, 709, 710, 714, 707, 707, 730, 707, 707, 722, 709, 709, 712, 707, 711, 710, 711, 711, 707, 707, 707],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "real",
						"fieldCaption": "DAILY_PATIENTS",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[DAILY_PATIENTS]",
						"valueIndices": [0, 0, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -140, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 3, 0, 0, -140, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, -140, 0, 0, 0, 0, 0, 0, 0, 0, -140, -140, -140, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 0, 0, 0, 0, 3, 0, 0, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 3, 2, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 4, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 5, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
						"formatValIdxs": [715, 715, 718, 718, 717, 715, 715, 715, 715, 715, 715, 715, 718, 715, 715, 715, 715, 715, 718, 715, 715, 715, 715, 715, 715, 715, 718, 715, 718, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 718, 718, 715, 715, 718, 715, 715, 718, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 140, 715, 715, 715, 715, 715, 715, 715, 715, 718, 715, 718, 718, 715, 715, 140, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 718, 715, 715, 715, 715, 715, 715, 715, 715, 715, 140, 715, 715, 715, 715, 715, 715, 715, 715, 140, 140, 140, 715, 715, 715, 715, 715, 715, 715, 715, 718, 717, 715, 715, 715, 715, 718, 715, 715, 715, 717, 718, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 715, 718, 715, 715, 715, 718, 715, 718, 717, 715, 718, 715, 715, 715, 715, 715, 718, 715, 715, 715, 715, 715, 715, 715, 718, 715, 715, 715, 715, 715, 718, 715, 716, 715, 718, 715, 715, 715, 715, 715, 715, 718, 715, 715, 715, 715, 719, 715, 715, 715, 715, 718, 718, 715, 715, 715, 715, 715, 715, 715, 715],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "boolean",
						"fieldCaption": "EconRegion",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[Calculation_1832402148470874115]",
						"valueIndices": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						"formatValIdxs": [701, 701, 702, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 702, 701, 701, 701, 701, 701, 701, 701, 701, 701, 702, 701, 701, 701, 701, 701, 701, 701, 702, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 702, 701, 702, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 702, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701, 701],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "cstring",
						"fieldCaption": "Header",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[Calculation_1832402148466135040]",
						"valueIndices": [57, 58, 59, 60, 61, 62, 63, 64, 64, 62, 62, 62, 63, 63, 58, 58, 64, 64, 60, 60, 58, 65, 58, 57, 59, 61, 62, 60, 61, 63, 63, 60, 63, 64, 59, 62, 63, 65, 57, 62, 65, 66, 59, 66, 64, 58, 61, 62, 64, 64, 65, 62, 66, 62, 60, 62, 62, 62, 63, 66, 63, 62, 62, 62, 62, 58, 62, 57, 66, 62, 62, 66, 62, 62, 60, 57, 58, 65, 63, 62, 63, 63, 66, 62, 64, 63, 62, 62, 62, 62, 64, 64, 64, 62, 62, 62, 62, 62, 62, 66, 62, 63, 62, 62, 62, 62, 62, 62, 66, 66, 57, 62, 62, 62, 62, 64, 62, 62, 64, 62, 65, 63, 65, 62, 66, 64, 64, 60, 63, 61, 64, 61, 60, 66, 64, 66, 64, 62, 62, 58, 65, 57, 62, 64, 64, 59, 58, 59, 60, 63, 63, 65, 66, 66, 64, 66, 57, 66, 62, 64, 59, 66, 60, 66, 60, 61, 64, 57, 57, 62, 62, 65, 66, 65, 65, 58, 58, 58, 58, 63, 61, 60, 60, 65, 65, 66, 66, 66, 61, 62, 64, 64, 63, 64, 64, 62, 62, 65, 57, 58],
						"formatValIdxs": [57, 58, 59, 60, 61, 62, 63, 64, 64, 62, 62, 62, 63, 63, 58, 58, 64, 64, 60, 60, 58, 65, 58, 57, 59, 61, 62, 60, 61, 63, 63, 60, 63, 64, 59, 62, 63, 65, 57, 62, 65, 66, 59, 66, 64, 58, 61, 62, 64, 64, 65, 62, 66, 62, 60, 62, 62, 62, 63, 66, 63, 62, 62, 62, 62, 58, 62, 57, 66, 62, 62, 66, 62, 62, 60, 57, 58, 65, 63, 62, 63, 63, 66, 62, 64, 63, 62, 62, 62, 62, 64, 64, 64, 62, 62, 62, 62, 62, 62, 66, 62, 63, 62, 62, 62, 62, 62, 62, 66, 66, 57, 62, 62, 62, 62, 64, 62, 62, 64, 62, 65, 63, 65, 62, 66, 64, 64, 60, 63, 61, 64, 61, 60, 66, 64, 66, 64, 62, 62, 58, 65, 57, 62, 64, 64, 59, 58, 59, 60, 63, 63, 65, 66, 66, 64, 66, 57, 66, 62, 64, 59, 66, 60, 66, 60, 61, 64, 57, 57, 62, 62, 65, 66, 65, 65, 58, 58, 58, 58, 63, 61, 60, 60, 65, 65, 66, 66, 66, 61, 62, 64, 64, 63, 64, 64, 62, 62, 65, 57, 58],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "date",
						"fieldCaption": "Last Updated Date",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[Calculation_954763183074803712]",
						"valueIndices": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
						"formatValIdxs": [731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 731, 703, 703],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "integer",
						"fieldCaption": "Number of Records",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[Number of Records]",
						"valueIndices": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						"formatValIdxs": [710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710, 710],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "real",
						"fieldCaption": "TOTAL_DEATH",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[TOTAL_DEATH]",
						"valueIndices": [12, 3, 18, 19, 17, 20, 11, 0, 21, 22, 23, 24, 25, 26, 25, 13, 27, 0, 28, 12, 29, 7, 0, 6, 30, 14, 31, 32, 33, 3, 0, 3, 29, 2, 34, 35, 36, 37, 38, 39, 25, 40, 41, 42, 43, 0, 44, 45, 30, 2, 46, 7, 47, 48, 4, 49, 50, 0, 0, 51, 52, 53, 54, 0, 55, 8, 56, 1, 57, 58, 59, 60, 0, 61, 0, 62, 3, 6, 12, 63, 0, 64, 65, 66, 67, 68, 69, 70, 0, 71, 37, 72, 73, 3, 74, 58, 59, 75, 76, 77, 78, 79, 0, 0, 0, 0, 80, 81, 82, 83, 84, 85, 86, 87, 88, 60, 33, 89, 72, 90, 91, 92, 79, 93, 94, 28, 95, 0, 96, 28, 97, 29, 98, 99, 100, 101, 30, 102, 102, 0, 103, 104, 105, 0, 106, 107, 108, 109, 0, 110, 111, 5, 0, 81, 17, 112, 113, 114, 115, 116, 117, 118, 13, 119, 0, 120, 121, 122, 4, 123, 67, 86, 124, 33, 0, 1, 108, 1, 3, 125, 126, 11, 127, 0, 128, 129, 7, 130, 131, 132, 133, 117, 2, 134, 3, 135, 136, 10, 12, 3],
						"formatValIdxs": [732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 744, 746, 747, 739, 748, 732, 749, 750, 739, 751, 752, 753, 754, 755, 756, 733, 739, 733, 749, 757, 758, 759, 760, 761, 762, 763, 744, 764, 765, 766, 767, 739, 768, 769, 752, 757, 770, 750, 771, 772, 773, 774, 775, 739, 739, 776, 777, 778, 779, 739, 780, 781, 782, 783, 784, 785, 786, 787, 739, 788, 739, 789, 733, 751, 732, 790, 739, 791, 792, 793, 794, 795, 796, 797, 739, 798, 761, 799, 800, 733, 801, 785, 786, 802, 803, 804, 805, 806, 739, 739, 739, 739, 807, 808, 809, 810, 811, 812, 813, 814, 815, 787, 756, 816, 799, 817, 818, 819, 806, 820, 821, 748, 822, 739, 823, 748, 824, 749, 825, 826, 827, 828, 752, 829, 829, 739, 830, 831, 832, 739, 833, 834, 835, 836, 739, 837, 838, 839, 739, 808, 736, 840, 841, 842, 843, 844, 845, 846, 746, 847, 739, 848, 849, 850, 773, 851, 794, 813, 852, 756, 739, 783, 835, 783, 733, 853, 854, 738, 855, 739, 856, 857, 750, 858, 859, 860, 861, 845, 757, 862, 733, 863, 864, 865, 732, 733],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}, {
						"dataType": "real",
						"fieldCaption": "TOTAL_DISCHARGE",
						"fn": "[federated.05hfglv18oi9571bhp1mu1gb9wja].[TOTAL_DISCHARGE]",
						"valueIndices": [74, 41, 137, 138, 139, 140, 141, 12, 142, 143, 144, 145, 146, 147, 54, 27, 148, 46, 149, 150, 151, 40, 152, 110, 133, 46, 153, 154, 155, 156, 0, 157, 158, 151, 159, 160, 161, 71, 162, 163, 65, 164, 165, 166, 167, 5, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 0, 185, 186, 187, 188, 189, 190, 191, 192, 122, 193, 194, 195, 4, 196, 197, 198, 9, 199, 200, 201, 202, 203, 204, 205, 0, 206, 18, 207, 208, 152, 209, 210, 211, 212, 213, 214, 215, 216, 0, 0, 217, 0, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 60, 232, 233, 172, 234, 235, 236, 118, 115, 133, 237, 34, 22, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 91, 248, 249, 250, 251, 252, 253, 254, 255, 0, 256, 64, 257, 258, 259, 260, 261, 262, 263, 264, 265, 2, 266, 267, 268, 269, 270, 271, 272, 273, 274, 0, 275, 133, 276, 0, 277, 278, 279, 280, 0, 281, 282, 283, 284, 285, 172, 286, 287, 41, 288, 289, 290, 291, 292, 86, 41],
						"formatValIdxs": [801, 765, 866, 867, 868, 869, 870, 732, 871, 872, 873, 874, 875, 876, 779, 747, 877, 770, 878, 879, 880, 764, 881, 837, 861, 770, 882, 883, 884, 885, 739, 886, 887, 880, 888, 889, 890, 798, 891, 892, 792, 893, 894, 895, 896, 839, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 739, 914, 915, 916, 917, 918, 919, 920, 921, 850, 922, 923, 924, 773, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 739, 936, 734, 937, 938, 881, 939, 940, 941, 942, 943, 944, 945, 946, 739, 739, 947, 739, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 787, 962, 963, 901, 964, 965, 966, 846, 843, 861, 967, 758, 741, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 818, 978, 979, 980, 981, 982, 983, 984, 985, 739, 986, 791, 987, 988, 989, 990, 991, 992, 993, 994, 995, 757, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 739, 1005, 861, 1006, 739, 1007, 1008, 1009, 1010, 739, 1011, 1012, 1013, 1014, 1015, 901, 1016, 1017, 765, 1018, 1019, 1020, 1021, 1022, 813, 765],
						"aliasIndices": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
					}]
				}
			}
		}]
	}
}
"""

tableauDownloadableCsvData = """
COUNTY;CURRENT_ICU_PATIENTS;CURRENT_INTUBATED_PATIENTS;CURRENT_PATIENTS;Header;RegionFilter;EconRegion;Last Updated Date;DAILY_PATIENTS;ECON_REGION;FAC_LAT;FAC_LONG;HOSPITAL;HOSPITAL_NETWORK;NYC_IND;Nombre d'enregistrements;REGION;RPT_DT;SUB_REGION;TOTAL_DEATH;TOTAL_DISCHARGE
Otsego;0;0;0;Mohawk Valley;Faux;Faux;18/06/2021;0;Mohawk Valley;42.457405;-75.053261;A.O. Fox Memorial Hospital;Bassett Healthcare Network;;1;Capital District Regional Office;6/17/2021;Rest of State;12;289
Franklin;0;0;0;North Country;Faux;Faux;18/06/2021;0;North Country;44.343929;-74.144363;Adirondack Medical Center-Saranac Lake Site;Independent;;1;Capital District Regional Office;6/17/2021;Rest of State;1;49
Albany;5;2;11;Capital Region;Vrai;Vrai;18/06/2021;0;Capital Region;42.65337;-73.773834;Albany Medical Center Hospital;Albany Medical Center;;1;Capital District Regional Office;6/17/2021;Rest of State;249;1457
"""

tableauExportCrosstabServerDialog = """
{
	"vqlCmdResponse": {
		"layoutStatus": {
			"applicationPresModel": {
				"presentationLayerNotification": [{
					"presModelHolder": {
						"genExportCrosstabOptionsDialogPresModel": {
							"thumbnailSheetPickerItems": [{
								"thumbnailUri": "",
								"sheetName": "[WORKSHEET1]",
								"sheetdocId": "{XXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX}"
							}]
						}
					}
				}],
				"dashboardObjectsLibrary": []
			},
			"isWorldNew": false,
			"guid": ""
		}
	}
}
"""

tableauExportCrosstabToCsvServer = """
{
	"vqlCmdResponse": {
		"layoutStatus": {
			"applicationPresModel": {
				"presentationLayerNotification": [{
					"presModelHolder": {
						"genExportFilePresModel": {
							"resultKey": "3224154322"
						}
					}
				}]
			}
		}
	}
}
"""

tableauCrossTabData = """"
Header1 	Header2 	
1	A 	
2	B 	
3	C 	
"""

tableauStoryPointsInfoNav = {
    'sheetName': '[WORKSHEET1]',
    'worldUpdate': {
        'applicationPresModel': {
            'renderMode': 'render-mode-client',
            'workbookPresModel': {
                'dashboardPresModel': {
                    'sheetPath': {
                        'sheetName': '[WORKSHEET1]',
                        'isDashboard': True
                    },
                    'zones': {
                        '4': {
                            'zoneId': 4,
                            'zoneZOrder': 2,
                            'presModelHolder': {
                                'flipboardNav': {
                                    'currentStorypointIndex': 0,
                                    'storypointNavItems': [{
                                        'storyPointId': 1,
                                        'storyPointCaption': '1',
                                        'isCaptured': True,
                                        'storyPointIsEmpty': False,
                                        'containsValidDatasources': True
                                    }, {
                                        'storyPointId': 2,
                                        'storyPointCaption': '2',
                                        'isCaptured': True,
                                        'storyPointIsEmpty': False,
                                        'containsValidDatasources': True
                                    }, {
                                        'storyPointId': 3,
                                        'storyPointCaption': '3',
                                        'isCaptured': True,
                                        'storyPointIsEmpty': False,
                                        'containsValidDatasources': True
                                    }, {
                                        'storyPointId': 4,
                                        'storyPointCaption': '4',
                                        'isCaptured': True,
                                        'storyPointIsEmpty': False,
                                        'containsValidDatasources': True
                                    }, {
                                        'storyPointId': 5,
                                        'storyPointCaption': '5',
                                        'isCaptured': True,
                                        'storyPointIsEmpty': False,
                                        'containsValidDatasources': True
                                    }, {
                                        'storyPointId': 9,
                                        'storyPointCaption': '6',
                                        'isCaptured': True,
                                        'storyPointIsEmpty': False,
                                        'containsValidDatasources': True
                                    }, {
                                        'storyPointId': 10,
                                        'storyPointCaption': '7',
                                        'isCaptured': True,
                                        'storyPointIsEmpty': False,
                                        'containsValidDatasources': True
                                    }, {
                                        'storyPointId': 11,
                                        'storyPointCaption': '8',
                                        'isCaptured': True,
                                        'storyPointIsEmpty': False,
                                        'containsValidDatasources': True
                                    }, {
                                        'storyPointId': 8,
                                        'storyPointCaption': '9',
                                        'isCaptured': True,
                                        'storyPointIsEmpty': False,
                                        'containsValidDatasources': True
                                    }, {
                                        'storyPointId': 12,
                                        'storyPointCaption': '10',
                                        'isCaptured': True,
                                        'storyPointIsEmpty': False,
                                        'containsValidDatasources': True
                                    }, {
                                        'storyPointId': 13,
                                        'storyPointCaption': '11',
                                        'isCaptured': True,
                                        'storyPointIsEmpty': False,
                                        'containsValidDatasources': True
                                    }, {
                                        'storyPointId': 14,
                                        'storyPointCaption': '12',
                                        'isCaptured': True,
                                        'storyPointIsEmpty': False,
                                        'containsValidDatasources': True
                                    }],
                                    'navArrowsVisible': True,
                                    'spaceBetweenPoints': 2,
                                    'isStoryEmpty': False,
                                    'isPresentationModeDoc': False
                                }
                            },
                            'hasCaption': False,
                            'isVisible': True,
                            'isSelectionDisabled': True,
                            'bgColor': 'rgb(255,255,255)',
                            'blendedZoneContentColor': 'rgb(255,255,255)'
                        }
                    },
                },
            }
        }
    }
}

tableauDataResponseWithStoryPointsNav = """
433337;%s433337;%s
""" % (
    json.dumps(tableauStoryPointsInfoNav),
    json.dumps(dataWithoutPresModelWithDictionary),
)
