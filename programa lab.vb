sub main()
    Dim itruns as Boolean = True
    if itruns = True Then
        Dim persona() as String = {"Roberto", "sanchez", "ciudad de guatemala"}
        Dim clinicdata() as String = {"18kg", "163 cm", "O negativo"}
        Dim hasinsurance as Boolean = True
        Dim insurancenum as Integer = 25896412
        Dim Medic() as String = {"Jorge rosales", "Neuro cirujano", "Neurocirujia"}

        if hasinsurance = True Then:
            console.Writeline("=" * 5)
        else:
            console.Writeline("=" * 5)
            console.Writeline("No tiene seguro")                                  

    Else
        console.Writeline("el programa no funciona")
End sub