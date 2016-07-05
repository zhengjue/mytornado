#!/bin/env python
class Simple( object ):
        def __init__( self ):
            print( "constructor called, id={0}".format( id( self )))
        def __del__( self ):
            print( "destructor called, id={0}".format( id( self )))
        def __new__( self ):
            #print( "new called, id={0}".format( id( self )))
            return super( Simple, self ).__new__( self )

class Simple1( object ):
        def __init__( self ):
            print( "constructor called, id={0}".format( id( self )))
        def __del__( self ):
            print( "destructor called, id={0}".format( id( self )))
        def __new__( self ):
            print( "new called, id={0}".format( id( self )))
            #return super( Simple1, self ).__new__( self )
a=Simple()
b=Simple1()
