# -*- coding: utf-8 -*-

MONGO_MODES_DICT = {
    0: 'primary',
    1: 'primaryPreferred',
    2: 'secondary',
    3: 'secondaryPreferred',
    4: 'nearest',
}


# parsed['options']['readpreference'] = 'secondaryPreferred'
def patch(parsed_options):
    if isinstance(parsed_options, dict):
        if parsed_options.has_key('options'):
            options = parsed_options['options']
            if options.has_key('readpreference'):
                read_preference = options['readpreference']
                options['readpreference'] = MONGO_MODES_DICT[read_preference]
    return parsed_options

