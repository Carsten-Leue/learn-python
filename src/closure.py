from closure.closure import createClosure;

inc1 = createClosure("Carsten");
inc1();
inc1();

inc2 = createClosure("World");
inc2();
inc2();