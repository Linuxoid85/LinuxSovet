# Создание пользовательских интерфейсов

При построении более сложного пользовательского интерфейса с десятками или сотнями виджетов, выполнение всей работы по настройке в коде C является обременительным, а внесение изменений становится практически невозможным.

К счастью, GTK поддерживает отделение макета пользовательского интерфейса от логики программы, используя описания пользовательского интерфейса в формате XML, который может быть проанализирован классом `GtkBuilder`.

Создайте файл `example-3.c` и запишите в него следующее:
```c
#include <gtk/gtk.h>
#include <glib/gstdio.h>

static void
print_hello (GtkWidget *widget,
             gpointer   data)
{
  g_print ("Hello World\n");
}

static void
quit_cb (GtkWindow *window)
{
  gtk_window_close (window);
}

static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  /* Construct a GtkBuilder instance and load our UI description */
  GtkBuilder *builder = gtk_builder_new();
  gtk_builder_add_from_file (builder, "builder.ui", NULL);

  /* Connect signal handlers to the constructed widgets. */
  GObject *window = gtk_builder_get_object (builder, "window");
  gtk_window_set_application (GTK_WINDOW (window), app);

  GObject *button = gtk_builder_get_object (builder, "button1");
  g_signal_connect (button, "clicked", G_CALLBACK (print_hello), NULL);

  button = gtk_builder_get_object (builder, "button2");
  g_signal_connect (button, "clicked", G_CALLBACK (print_hello), NULL);

  button = gtk_builder_get_object (builder, "quit");
  g_signal_connect_swapped (button, "clicked", G_CALLBACK (quit_cb), window);

  gtk_widget_show (GTK_WIDGET (window));

  /* We do not need the builder any more */
  g_object_unref (builder);
}

int
main (int   argc,
      char *argv[])
{
#ifdef GTK_SRCDIR
  g_chdir (GTK_SRCDIR);
#endif

  GtkApplication *app = gtk_application_new ("org.gtk.example", G_APPLICATION_FLAGS_NONE);
  g_signal_connect (app, "activate", G_CALLBACK (activate), NULL);

  int status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);

  return status;
}
```

Так же, создайте файл `builder.ui` и запишите в него следующее:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object id="window" class="GtkWindow">
    <property name="title">Grid</property>
    <child>
      <object id="grid" class="GtkGrid">
        <child>
          <object id="button1" class="GtkButton">
            <property name="label">Button 1</property>
            <layout>
              <property name="column">0</property>
              <property name="row">0</property>
            </layout>
          </object>
        </child>
        <child>
          <object id="button2" class="GtkButton">
            <property name="label">Button 2</property>
            <layout>
              <property name="column">1</property>
              <property name="row">0</property>
            </layout>
          </object>
        </child>
        <child>
          <object id="quit" class="GtkButton">
            <property name="label">Quit</property>
            <layout>
              <property name="column">0</property>
              <property name="row">1</property>
              <property name="column-span">2</property>
            </layout>
          </object>
        </child>
      </object>
    </child>
  </object>
</interface>
```

Компиляция:
```bash
gcc `pkg-config --cflags gtk4` -o example-3 example-3.c `pkg-config --libs gtk4`
```

Обратите внимание, что `GtkBuilder` также может использоваться для создания объектов, которые не являются виджетами, таких как модели деревьев, корректировки и т.д. По этой причине метод, который мы здесь используем, называется `gtk_builder_get_object()` и возвращает `GObject*` вместо `GtkWidget*`.

Обычно вы передаете полный путь к `gtk_builder_add_from_file()`, чтобы выполнение вашей программы не зависело от текущего каталога. Обычно описания пользовательского интерфейса и аналогичные данные устанавливаются в `/usr/share/appname`.

Также можно встроить описание пользовательского интерфейса в исходный код в виде строки и использовать `gtk_builder_add_from_string()` для его загрузки. Но хранение описания пользовательского интерфейса в отдельном файле имеет несколько преимуществ: тогда можно внести незначительные изменения в пользовательский интерфейс без перекомпиляции вашей программы, и, что более важно, графические редакторы пользовательского интерфейса, такие как glade, могут загрузить файл и позволить вам создавать и измените свой пользовательский интерфейс, щелкнув мышью, т.е. - интерактивно и очень просто.

***
[Назад - пользовательский рисунок](gtk4.md)

[Далее - создание приложений - часть 1. Тривиальное приложение, открытие файлов...](gtk6.md)
