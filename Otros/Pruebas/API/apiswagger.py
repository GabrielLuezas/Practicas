import yaml

swagger_template = {
    'swagger': '2.0',
    'info': {
        'title': 'API de Usuarios',
        'description': 'API para gestionar usuarios',
        'version': '1.0'
    },
    'paths': {
        '/usuarios': {
            'get': {
                'summary': 'Obtener todos los usuarios',
                'responses': {
                    '200': {
                        'description': 'Lista de usuarios',
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'Usuarios': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object'
                                    }
                                }
                            }
                        }
                    }
                }
            },
            'post': {
                'summary': 'Agregar un nuevo usuario',
                'parameters': [
                    {
                        'name': 'body',
                        'in': 'body',
                        'description': 'Datos del usuario',
                        'required': True,
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': 'string'
                                },
                                'nombre': {
                                    'type': 'string'
                                },
                                'apellido': {
                                    'type': 'string'
                                },
                                'edad': {
                                    'type': 'integer'
                                }
                            }
                        }
                    }
                ],
                'responses': {
                    '200': {
                        'description': 'Usuario añadido a Mongo'
                    }
                }
            }
        },
        '/usuarios/{nombre_usuario}': {
            'get': {
                'summary': 'Obtener usuarios por nombre',
                'parameters': [
                    {
                        'name': 'nombre_usuario',
                        'in': 'path',
                        'description': 'Nombre del usuario',
                        'required': True,
                        'type': 'string'
                    }
                ],
                'responses': {
                    '200': {
                        'description': 'Lista de usuarios encontrados',
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'usuarios': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object'
                                    }
                                }
                            }
                        }
                    },
                    '404': {
                        'description': 'No se encontraron usuarios con el nombre especificado'
                    }
                }
            },
            'delete': {
                'summary': 'Eliminar usuario por nombre',
                'parameters': [
                    {
                        'name': 'nombre_usuario',
                        'in': 'path',
                        'description': 'Nombre del usuario',
                        'required': True,
                        'type': 'string'
                    }
                ],
                'responses': {
                    '200': {
                        'description': 'Usuario borrado con éxito'
                    },
                    '404': {
                        'description': 'No hay documentos con ese nombre'
                    }
                }
            }
        },
        '/usuarios/{nombre_usuario}/{id_usuario}': {
            'get': {
                'summary': 'Obtener usuario por nombre e ID',
                'parameters': [
                    {
                        'name': 'nombre_usuario',
                        'in': 'path',
                        'description': 'Nombre del usuario',
                        'required': True,
                        'type': 'string'
                    },
                    {
                        'name': 'id_usuario',
                        'in': 'path',
                        'description': 'ID del usuario',
                        'required': True,
                        'type': 'string'
                    }
                ],
                'responses': {
                    '200': {
                        'description': 'Usuario encontrado',
                        'schema': {
                            'type': 'object'
                        }
                    },
                    '404': {
                        'description': 'No se encontró el usuario con el nombre y ID especificados'
                    }
                }
            },
            'put': {
                'summary': 'Actualizar usuario por nombre',
                'parameters': [
                    {
                        'name': 'nombre_usuario',
                        'in': 'path',
                        'description': 'Nombre del usuario',
                        'required': True,
                        'type': 'string'
                    },
                    {
                        'name': 'body',
                        'in': 'body',
                        'description': 'Datos del usuario',
                        'required': True,
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'nombre': {
                                    'type': 'string'
                                },
                                'apellido': {
                                    'type': 'string'
                                },
                                'edad': {
                                    'type': 'integer'
                                }
                            }
                        }
                    }
                ],
                'responses': {
                    '200': {
                        'description': 'Documento actualizado correctamente'
                    },
                    '404': {
                        'description': 'No hay documentos con ese nombre'
                    }
                }
            },
            'delete': {
                'summary': 'Eliminar usuario por nombre e ID',
                'parameters': [
                    {
                        'name': 'nombre_usuario',
                        'in': 'path',
                        'description': 'Nombre del usuario',
                        'required': True,
                        'type': 'string'
                    },
                    {
                        'name': 'id_usuario',
                        'in': 'path',
                        'description': 'ID del usuario',
                        'required': True,
                        'type': 'string'
                    }
                ],
                'responses': {
                    '200': {
                        'description': 'Usuario borrado con éxito'
                    },
                    '404': {
                        'description': 'No hay documentos con ese nombre e ID'
                    }
                }
            }
        },
        '/interfaz': {
            'get': {
                'summary': 'Mostrar interfaz',
                'responses': {
                    '200': {
                        'description': 'Interfaz mostrada correctamente'
                    }
                }
            },
            'post': {
                'summary': 'Insertar datos en la base de datos',
                'parameters': [
                    {
                        'name': 'body',
                        'in': 'body',
                        'description': 'Datos del usuario',
                        'required': True,
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'nombre': {
                                    'type': 'string'
                                },
                                'apellido': {
                                    'type': 'string'
                                },
                                'edad': {
                                    'type': 'string'
                                }
                            }
                        }
                    }
                ],
                'responses': {
                    '200': {
                        'description': 'Datos insertados en la base de datos correctamente'
                    }
                }
            }
        }
    }
}

with open('swagger.yaml', 'w') as file:
    yaml.dump(swagger_template, file)