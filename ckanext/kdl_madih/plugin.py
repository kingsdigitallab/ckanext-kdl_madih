import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def madih_kdl_project_status():
    create_kdl_project_status()

    try:
        tag_list = toolkit.get_action("tag_list")
        return tag_list(data_dict={"vocabulary_id": "madih_kdl_project_status"})
    except toolkit.ObjectNotFound:
        return None


def create_kdl_project_status():
    user = toolkit.get_action("get_site_user")({"ignore_auth": True}, {})
    context = {"user": user["name"]}

    try:
        data = {"id": "madih_kdl_project_status"}
        toolkit.get_action("vocabulary_show")(context, data)
    except toolkit.ObjectNotFound:
        data = {"name": "madih_kdl_project_status"}
        vocab = toolkit.get_action("vocabulary_create")(context, data)
        for tag in (u"Completed", u"Ongoing"):
            data = {"name": tag, "vocabulary_id": vocab["id"]}
            toolkit.get_action("tag_create")(context, data)


MADIH_KDL_DATATYPE = "madih_kdl_datatype"


def madih_kdl_datatype():
    create_madih_kdl_datatype()

    try:
        tag_list = toolkit.get_action("tag_list")
        return tag_list(data_dict={"vocabulary_id": MADIH_KDL_DATATYPE})
    except toolkit.ObjectNotFound:
        return None


def create_madih_kdl_datatype():
    user = toolkit.get_action("get_site_user")({"ignore_auth": True}, {})
    context = {"user": user["name"]}

    data = {"id": MADIH_KDL_DATATYPE}

    try:
        vocab = toolkit.get_action("vocabulary_show")(context, data)
    except toolkit.ObjectNotFound:
        data = {"name": MADIH_KDL_DATATYPE}
        vocab = toolkit.get_action("vocabulary_create")(context, data)

    vocab_id = vocab["id"]
    datatypes = [
        "Databases",
        "Tables",
        "Images Aerial photograph",
        "Images Satellite image",
        "Images Photograph",
        "Images Plan or Sketch",
        "Images Section Drawing",
        "Images Map",
        "Images Artefact Drawing",
        "Structured graphics-models 3D model",
        "Structured graphics-models Photogrammetric model",
        "Structured graphics-models Virtual Reality",
        "Audiovisual data Recording",
        "Audiovisual data Video",
        "Scientific and statistical data formats",
        "Text article",
        "Text letter",
        "Text manuscript",
        "Text periodical",
        "Text newspaper",
        "Text legal article",
        "Text essay",
        "Text technical report",
        "Text report",
        "Text poetry",
        "Text postcard",
        "Text Oral History Transcript",
        "Text Diary/Notebook",
        "Text book",
        "Text autobiography",
        "Archived data",
        "Software applications",
        "Other",
    ]

    for name in datatypes:
        try:
            data = {"name": name, "vocabulary_id": vocab_id}
            toolkit.get_action("tag_create")(context, data)
        except toolkit.ValidationError:
            pass


def madih_kdl_time_periods():
    create_time_periods()
    try:
        tag_list = toolkit.get_action("tag_list")
        return tag_list(data_dict={"vocabulary_id": "madih_kdl_time_periods"})
    except toolkit.ObjectNotFound:
        return None


def create_time_periods():
    user = toolkit.get_action("get_site_user")({"ignore_auth": True}, {})
    context = {"user": user["name"]}

    try:
        data = {"id": "madih_kdl_time_periods"}
        vocab = toolkit.get_action("vocabulary_show")(context, data)
    except toolkit.ObjectNotFound:
        data = {"name": "madih_kdl_time_periods"}
        vocab = toolkit.get_action("vocabulary_create")(context, data)
    for tag in (
        u"Palaeolithic Unspecified",
        u"Palaeolithic Lower",
        u"Palaeolithic Middle",
        u"Palaeolithic Upper",
        u"Epi-Palaeolithic Unspecified",
        u"Epi-Palaeolithic Kebaran",
        u"Epi-Palaeolithic Natufian",
        u"Neolithic Unspecified",
        u"Neolithic Pre-Pottery Early",
        u"Neolithic Pre-Pottery A",
        u"Neolithic Pre-Pottery B",
        u"Neolithic Pre-Pottery C",
        u"Neolithic Pottery Late",
        u"Neolithic Pottery A Yarmukian",
        u"Neolithic Pottery B",
        u"Chalcolithic Unspecified",
        u"Chalcolithic Early",
        u"Chalcolithic Late",
        u"Bronze Age Unspecified",
        u"Early Bronze Age",
        u"Early Bronze Age I",
        u"Early Bronze Age II",
        u"Early Bronze Age III",
        u"Early Bronze Age IV",
        u"Middle Bronze Age",
        u"Late Bronze Age",
        u"Iron Age unspecified",
        u"Iron Age I",
        u"Iron Age II",
        u"Iron Age III",
        u"Persian",
        u"Hellenistic",
        u"Nabataean",
        u"Nabataean Early",
        u"Nabataean Middle",
        u"Nabataean Late",
        u"Roman",
        u"Roman Early",
        u"Roman Late",
        u"Byzantine",
        u"Byzantine Early",
        u"Byzantine Late",
        u"Islamic Unspecified",
        u"Islamic Early",
        u"Islamic Early Umayyad",
        u"Islamic Early Abbasid",
        u"Islamic Middle",
        u"Islamic Middle Fatimid",
        u"Islamic Middle Ayyubid",
        u"Islamic Middle Crusader",
        u"Islamic Late Mamluk",
        u"Islamic Ottoman",
        u"Islamic Ottoman Early",
        u"Islamic Ottoman Late",
        u"Modern",
        u"Hashemite",
        u"Period Unknown or Unspecified",
    ):
        try:
            data = {"name": tag, "vocabulary_id": vocab["id"]}
            toolkit.get_action("tag_create")(context, data)
        except toolkit.ValidationError:
            pass


class Kdl_MadihPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IFacets)

    # Add time period to facets on left
    def dataset_facets(self, facets_dict, package_type):
        facets_dict["vocab_madih_kdl_time_periods"] = plugins.toolkit._("Time Periods")
        facets_dict["vocab_madih_kdl_project_status"] = plugins.toolkit._(
            "Project Status"
        )
        return facets_dict

    # Currently not changed, may if search is needed
    def group_facets(self, facets_dict, group_type, package_type):
        return facets_dict

    # Currently not changed, may if search is needed
    def organization_facets(self, facets_dict, organization_type, package_type):
        return facets_dict

    def get_helpers(self):
        return {
            "madih_kdl_time_periods": madih_kdl_time_periods,
            "madih_kdl_project_status": madih_kdl_project_status,
            MADIH_KDL_DATATYPE: madih_kdl_datatype,
        }

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("fanstatic", "kdl_madih")

    def _modify_package_schema(self, schema):
        schema.update(
            {
                "madih_kdl_time_periods": [
                    toolkit.get_converter("convert_to_tags")("madih_kdl_time_periods")
                ],
                MADIH_KDL_DATATYPE: [
                    toolkit.get_converter("convert_to_tags")(MADIH_KDL_DATATYPE)
                ],
                "madih_kdl_project_url": [
                    toolkit.get_validator("ignore_missing"),
                    toolkit.get_validator("url_validator"),
                    toolkit.get_converter("convert_to_extras"),
                ],
                "madih_kdl_project_pi": [
                    toolkit.get_validator("ignore_missing"),
                    toolkit.get_converter("convert_to_extras"),
                ],
                "madih_kdl_project_team": [
                    toolkit.get_validator("ignore_missing"),
                    toolkit.get_converter("convert_to_extras"),
                ],
                "madih_kdl_project_start_date": [
                    toolkit.get_validator("ignore_missing"),
                    toolkit.get_converter("convert_to_extras"),
                ],
                "madih_kdl_project_end_date": [
                    toolkit.get_validator("ignore_missing"),
                    toolkit.get_converter("convert_to_extras"),
                ],
                "madih_kdl_project_status": [
                    toolkit.get_converter("convert_to_tags")("madih_kdl_project_status")
                ],
                "madih_kdl_project_funder": [
                    toolkit.get_validator("ignore_missing"),
                    toolkit.get_converter("convert_to_extras"),
                ],
                "madih_kdl_project_citation": [
                    toolkit.get_validator("ignore_missing"),
                    toolkit.get_converter("convert_to_extras"),
                ],
            }
        )
        return schema

    def show_package_schema(self):
        schema = super(Kdl_MadihPlugin, self).show_package_schema()

        schema["tags"]["__extras"].append(toolkit.get_converter("free_tags_only"))

        schema.update(
            {
                "madih_kdl_time_periods": [
                    toolkit.get_converter("convert_from_tags")("madih_kdl_time_periods")
                ],
                MADIH_KDL_DATATYPE: [
                    toolkit.get_converter("convert_from_tags")(MADIH_KDL_DATATYPE)
                ],
                "madih_kdl_project_url": [
                    toolkit.get_converter("convert_from_extras"),
                    toolkit.get_validator("url_validator"),
                    toolkit.get_validator("ignore_missing"),
                ],
                "madih_kdl_project_pi": [
                    toolkit.get_converter("convert_from_extras"),
                    toolkit.get_validator("ignore_missing"),
                ],
                "madih_kdl_project_team": [
                    toolkit.get_converter("convert_from_extras"),
                    toolkit.get_validator("ignore_missing"),
                ],
                "madih_kdl_project_start_date": [
                    toolkit.get_converter("convert_from_extras"),
                    toolkit.get_validator("ignore_missing"),
                ],
                "madih_kdl_project_end_date": [
                    toolkit.get_converter("convert_from_extras"),
                    toolkit.get_validator("ignore_missing"),
                ],
                "madih_kdl_project_status": [
                    toolkit.get_converter("convert_from_tags")(
                        "madih_kdl_project_status"
                    ),
                ],
                "madih_kdl_project_funder": [
                    toolkit.get_converter("convert_from_extras"),
                    toolkit.get_validator("ignore_missing"),
                ],
                "madih_kdl_project_citation": [
                    toolkit.get_converter("convert_from_extras"),
                    toolkit.get_validator("ignore_missing"),
                ],
            }
        )
        return schema

    def create_package_schema(self):
        schema = super(Kdl_MadihPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(Kdl_MadihPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
