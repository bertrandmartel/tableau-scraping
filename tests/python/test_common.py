import json

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
                    }
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
